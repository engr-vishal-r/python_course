# gs://<bucket>/jobs/extract_employee.py
import argparse
import logging
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
import hashlib
import sys
import os

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger("extract_employee")

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--gcs_output", required=True)
    p.add_argument("--last_watermark", required=True)
    p.add_argument("--new_watermark", required=True)
    p.add_argument("--jdbc_url", default=os.environ.get("JDBC_URL"))
    p.add_argument("--jdbc_user", default=os.environ.get("JDBC_USER"))
    p.add_argument("--jdbc_password", default=os.environ.get("JDBC_PASSWORD"))
    return p.parse_args()

def main():
    args = parse_args()
    spark = SparkSession.builder.appName("extract_employee").getOrCreate()
    # Idempotent extract: query using last_watermark and new_watermark
    LOG.info("Extracting records between %s and %s", args.last_watermark, args.new_watermark)
    query = f"(SELECT *, updated_at as _updated_at FROM employee WHERE updated_at > TIMESTAMP('{args.last_watermark}') AND updated_at <= TIMESTAMP('{args.new_watermark}')) tmp"
    df = spark.read.format("jdbc")\
        .option("url", args.jdbc_url)\
        .option("dbtable", query)\
        .option("user", args.jdbc_user)\
        .option("password", args.jdbc_password)\
        .option("fetchsize", "10000")\
        .load()
    # add metadata columns
    df = df.withColumn("_ingest_ts", lit(args.new_watermark))
    # compute hash for dedupe and SCD change detection
    from pyspark.sql.functions import sha2, concat_ws
    df = df.withColumn("_hash", sha2(concat_ws("||", *df.columns), 256))
    out_path = os.path.join(args.gcs_output, f"ingest_dt={args.new_watermark.split('T')[0]}", f"wm={args.new_watermark}")
    # Write idempotent: overwrite the specific watermark partition
    df.repartition(10).write.mode("overwrite").parquet(out_path)
    # write a success file
    spark.sparkContext.parallelize([1]).saveAsTextFile(out_path + "/_SUCCESS")
    LOG.info("Wrote %d rows to %s", df.count(), out_path)
    spark.stop()

if __name__ == "__main__":
    main()
