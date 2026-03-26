CREATE TABLE IF NOT EXISTS metadata.watermarks (
  table_name STRING NOT NULL,
  last_watermark TIMESTAMP NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);