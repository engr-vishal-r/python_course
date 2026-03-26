# gs://<bucket>/jobs/transform_employee.py
import argparse
import logging
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window
from pyspark import StorageLevel
import os

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger("transform_employee")

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--bronze_path", required=True)
    p.add_argument("--silver_path", required=True)
    p.add_argument("--ingest_date", required=True)
    return p.parse_args()

def main():
    args = parse_args()
    spark = SparkSession.builder.appName("transform_employee") \
        .config("spark.sql.shuffle.partitions", "200") \
        .config("spark.sql.adaptive.enabled", "true") \
        .getOrCreate()

    # Enable checkpoint directory on GCS for long lineage
    spark.sparkContext.setCheckpointDir("gs://{}/spark-checkpoints/".format(os.environ.get("GCS_BUCKET")))
    bronze_glob = os.path.join(args.bronze_path, f"ingest_dt={args.ingest_date}/*")
    LOG.info("Reading bronze path: %s", bronze_glob)
    df = spark.read.parquet(bronze_glob)

    # Basic cleaning from your script, but production-grade:
    # - Use strict date parsing with to_date + try/catch patterns,
    # - Avoid select *; explicitly pick columns
    # Example transforms
    pattern = r"[a-z0-9._-]+@[a-z]+\.(co|com|org|in)$"
    df = (df
          .drop("password", "phone")
          .fillna({"bonus": -1})
          .withColumn("email_id", when(col("email").rlike(pattern), col("email")).otherwise("Invalid Email"))
          .withColumn("dob_dt", to_date(col("dob"), "dd-MM-yyyy"))
          .withColumn("age", floor(months_between(current_date(), col("dob_dt"))/12))
          .filter(col("age") >= 18)
          .filter(col("department").isNotNull())
          .withColumn("total_compensation", coalesce(col("salary"), lit(0)) + coalesce(col("bonus"), lit(0)))
          .withColumn("tax", col("salary") * lit(0.01))
          .withColumn("service", when(col("is_active") == "Y", "In Service").otherwise("Not In Service"))
          .withColumn("emp_type",
                      when((col("yex") >= 10) & (col("yex") <= 12), "Senior")
                      .when((col("yex") < 10) & (col("yex") >= 5), "Intermediate")
                      .otherwise("Junior"))
          .withColumn("emp_name", upper(concat(col("fname"), lit(" "), col("lname"))))
         )

    # Storage Level: cache if reused multiple times
    df.persist(StorageLevel.MEMORY_AND_DISK)

    # window ops - careful with large partitions; use partitionBy department
    window_rank = Window.partitionBy("department").orderBy(col("salary").desc())
    # for cumulative sum use rangeBetween or use an efficient aggregation
    # Use checkpoint if lineage too long
    df = (df
          .withColumn("dense_rank", dense_rank().over(window_rank))
          .withColumn("cumulative_sum", sum(col("salary")).over(window_rank.rowsBetween(Window.unboundedPreceding, Window.currentRow)))
         )
    # top per department
    dense_df = df.filter(col("dense_rank") == 1)

    # Repartition to avoid small files and handle skew:
    # If department is skewed, we can salt key or broadcast small side joins (shown later)
    out_path = os.path.join(args.silver_path, f"ingest_dt={args.ingest_date}")
    # coalesce to a controlled number of files (e.g., 50)
    df_to_write = df.repartition(50, col("department"))
    # write as partitioned parquet/Delta
    (df_to_write.write
        .mode("overwrite")
        .option("parquet.enable.summary-metadata", "false")
        .partitionBy("department", "ingest_dt")
        .option("mergeSchema", "true")  # allows schema evolution for parquet (if using Delta prefer delta table)
        .parquet(out_path)
    )

    # write a manifest / success marker
    spark.sparkContext.parallelize([1]).saveAsTextFile(out_path + "/_SUCCESS")
    LOG.info("Wrote transformed data to %s", out_path)
    df.unpersist()
    spark.stop()

if __name__ == "__main__":
    main()
