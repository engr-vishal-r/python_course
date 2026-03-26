from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, current_date
from pyspark.sql.types import DateType

# --------------------------------------------------
# 1. Create Spark Session
# --------------------------------------------------
spark = SparkSession.builder \
    .appName("pyspark_scd2_incremental") \
    .master("local[*]") \
    .getOrCreate()

# --------------------------------------------------
# 2. Target Data (Existing Table)
# --------------------------------------------------
target_data = [
    (1, "vishal", "chennai"),
    (2, "ajay", "villupuram"),
    (3, "ramesh", "vellore")
]

schema = ["id", "name", "city"]

target_df = spark.createDataFrame(target_data, schema)

# Add SCD columns
target_df = target_df \
    .withColumn("start_date", current_date()) \
    .withColumn("end_date", lit("9999-12-31").cast(DateType())) \
    .withColumn("is_current", lit("Y"))

print("==== TARGET TABLE ====")
target_df.show()

# --------------------------------------------------
# 3. Source Data (New Incremental Data)
# --------------------------------------------------
src_data = [
    (1, "vishal", "bangalore"),   # updated
    (2, "ajay", "villupuram"),    # unchanged
    (4, "dinesh", "villupuram")   # new
]

src_df = spark.createDataFrame(src_data, schema)

print("==== SOURCE TABLE ====")
src_df.show()

# --------------------------------------------------
# 4. Join Target & Source
# --------------------------------------------------
joined_df = target_df.alias("t") \
    .join(src_df.alias("s"),
          col("t.id") == col("s.id"),
          "fullouter")

# --------------------------------------------------
# 5. Records to Expire (Updated Records)
# --------------------------------------------------
expire_df = joined_df.filter(
    (col("t.id").isNotNull()) &
    (col("s.id").isNotNull()) &
    (col("t.city") != col("s.city")) &
    (col("t.is_current") == "Y")
).select("t.*") \
 .withColumn("end_date", current_date()) \
 .withColumn("is_current", lit("N"))

# --------------------------------------------------
# 6. New Version of Updated Records
# --------------------------------------------------
new_version_df = joined_df.filter(
    (col("t.id").isNotNull()) &
    (col("s.id").isNotNull()) &
    (col("t.city") != col("s.city"))
).select(
    col("s.id").alias("id"),
    col("s.name").alias("name"),
    col("s.city").alias("city")
).withColumn("start_date", current_date()) \
 .withColumn("end_date", lit("9999-12-31").cast(DateType())) \
 .withColumn("is_current", lit("Y"))

# --------------------------------------------------
# 7. Completely New Records
# --------------------------------------------------
new_records_df = joined_df.filter(
    col("t.id").isNull() & col("s.id").isNotNull()
).select(
    col("s.id").alias("id"),
    col("s.name").alias("name"),
    col("s.city").alias("city")
).withColumn("start_date", current_date()) \
 .withColumn("end_date", lit("9999-12-31").cast(DateType())) \
 .withColumn("is_current", lit("Y"))

# --------------------------------------------------
# 8. Unchanged Records
# --------------------------------------------------
unchanged_df = joined_df.filter(
    (col("t.id").isNotNull()) &
    (col("s.id").isNotNull()) &
    (col("t.city") == col("s.city"))
).select("t.*")

# --------------------------------------------------
# 9. Records Present Only in Target (Deleted in Source)
# (Optional: keep as historical)
# --------------------------------------------------
target_only_df = joined_df.filter(
    col("t.id").isNotNull() & col("s.id").isNull()
).select("t.*")

# --------------------------------------------------
# 10. Final SCD2 Table
# --------------------------------------------------
final_df = expire_df \
    .unionByName(new_version_df) \
    .unionByName(new_records_df) \
    .unionByName(unchanged_df) \
    .unionByName(target_only_df)

print("==== FINAL SCD2 TABLE ====")
final_df.orderBy("id", "start_date").show(truncate=False)