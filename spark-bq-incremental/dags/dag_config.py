PROJECT_ID = "my-project"
REGION = "us-central1"
CLUSTER = "spark-cluster"

TABLE_CONFIG = {
    "trips": {
        "raw_path": "gs://bucket/raw/trips/",
        "temp_path": "gs://bucket/temp/trips/",
        "bq_table": "analytics.trips",
        "watermark_column": "updated_at"
    },
    "payments": {
        "raw_path": "gs://bucket/raw/payments/",
        "temp_path": "gs://bucket/temp/payments/",
        "bq_table": "analytics.payments",
        "watermark_column": "updated_at"
    }
}

BQ_WATERMARK_TABLE = "metadata.watermarks"
BQ_ERROR_TABLE = "metadata.spark_errors"
SPARK_MAIN = "gs://bucket/spark_jobs/main.py"
