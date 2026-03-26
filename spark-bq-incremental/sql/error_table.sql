CREATE TABLE IF NOT EXISTS metadata.spark_errors (
  table_name STRING,
  error_reason STRING,
  raw_record STRING,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);