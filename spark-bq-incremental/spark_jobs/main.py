import argparse
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, max as spark_max
from pyspark import StorageLevel

from utils.logging_utils import get_logger
from schemas.schema import get_schema
from transform import transform
from watermark import get_watermark, update_watermark
from error_logger import write_errors
from utils.udf_utils import register_udfs

LOOKBACK_DAYS = 3


def main():
    args = parse_args()

    spark = (
        SparkSession.builder
        .appName(args.table)
        .config("spark.sql.shuffle.partitions", "200")
        .getOrCreate()
    )

    spark.sparkContext.setCheckpointDir("gs://bucket/checkpoints")

    register_udfs(spark)
    logger = get_logger(args.table)

    # -----------------------------------
    # 1️⃣ Get watermark
    # -----------------------------------
    watermark = get_watermark(args.table)
    logger.info(f"Using watermark: {watermark}")

    # -----------------------------------
    # 2️⃣ Read raw CSV (without schema first)
    # -----------------------------------
    raw_df = (
        spark.read
        .option("header", True)
        .csv(f"gs://bucket/raw/{args.table}/")
    )

    expected_schema = get_schema(args.table)
    expected_columns = {field.name for field in expected_schema.fields}
    incoming_columns = set(raw_df.columns)

    extra_columns = incoming_columns - expected_columns
    missing_columns = expected_columns - incoming_columns

    # Log schema drift
    from schema_drift_logger import write_schema_drift
    write_schema_drift(args.table, extra_columns, missing_columns)

    # Now enforce expected schema by selecting only expected columns
    df = raw_df.select(*expected_columns)
    df = spark.createDataFrame(df.rdd, expected_schema)

    # -----------------------------------
    # 3️⃣ Incremental filter
    # -----------------------------------
    df = df.filter(
        (col("updated_at") >= expr(
            f"TIMESTAMP_SUB(TIMESTAMP('{watermark}'), INTERVAL {LOOKBACK_DAYS} DAY)"
        )) &
        (col("updated_at") < expr(f"TIMESTAMP('{args.execution_date}')"))
    )

    # -----------------------------------
    # 4️⃣ Transform
    # -----------------------------------
    good_df, error_df = transform(df, spark)

    # -----------------------------------
    # 5️⃣ Persist (IMPORTANT)
    # -----------------------------------
    # good_df is used multiple times → persist
    good_df.persist(StorageLevel.MEMORY_AND_DISK)

    # error_df used for conditional write
    error_df.persist(StorageLevel.MEMORY_AND_DISK)

    # Materialize once to avoid recomputation
    good_df.count()
    error_df.count()

    # -----------------------------------
    # 6️⃣ Write error records efficiently
    # -----------------------------------
    if error_df.limit(1).count() > 0:
        write_errors(error_df, args.table, "INVALID_PRIMARY_KEY")

    # -----------------------------------
    # 7️⃣ Break lineage before write (optional but safe)
    # -----------------------------------
    good_df = good_df.checkpoint()

    # -----------------------------------
    # 8️⃣ Write good records
    # -----------------------------------
    good_df.write \
        .mode("append") \
        .parquet(f"gs://bucket/temp/{args.table}/")

    # -----------------------------------
    # 9️⃣ Update watermark safely
    # -----------------------------------
    max_row = good_df.select(spark_max("updated_at")).first()
    new_wm = max_row[0] if max_row else None

    if new_wm:
        update_watermark(args.table, new_wm)
        logger.info(f"Updated watermark to: {new_wm}")

    # -----------------------------------
    # 🔟 Free memory
    # -----------------------------------
    good_df.unpersist()
    error_df.unpersist()

    spark.stop()


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--table", required=True)
    p.add_argument("--execution_date", required=True)
    return p.parse_args()


if __name__ == "__main__":
    main()