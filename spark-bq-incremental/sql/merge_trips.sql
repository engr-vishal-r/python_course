MERGE analytics.trips T
USING (SELECT * 
FROM analytics.trips_staging
WHERE DATE(updated_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY) S
ON T.trip_id = S.trip_id
AND DATE(T.updated_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)

WHEN MATCHED AND S.updated_at > T.updated_at THEN
  UPDATE SET
    trip_id      = S.trip_id,
    updated_at   = S.updated_at,
    amount       = S.amount,
    city         = S.city

WHEN NOT MATCHED THEN
  INSERT (
    trip_id,
    updated_at,
    amount,
    city
  )
  VALUES (
    S.trip_id,
    S.updated_at,
    S.amount,
    S.city
  );
