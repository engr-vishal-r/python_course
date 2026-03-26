SELECT
  MAX(updated_at) >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY)
FROM analytics.trips_staging;
