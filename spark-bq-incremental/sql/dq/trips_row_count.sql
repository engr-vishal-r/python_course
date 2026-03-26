SELECT COUNT(*) > 0
FROM analytics.trips_staging
WHERE DATE(updated_at) = DATE('{{ ds }}');
