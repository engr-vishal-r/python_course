SELECT COUNT(*) = 0
FROM (
  SELECT trip_id
  FROM analytics.trips_staging
  WHERE DATE(updated_at) = DATE('{{ ds }}')
  GROUP BY trip_id
  HAVING COUNT(*) > 1
);