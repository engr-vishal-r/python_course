from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("scd_test") \
    .master("local[*]") \
    .getOrCreate()

# Target data
target_data = [(1,"vishal","chennai"),
               (2,"ajay","villupuram"),
               (3,"ramesh","vellore")]

schema=["id","name","city"]

target_df = spark.createDataFrame(target_data, schema)

# Source data
src_data = [(1,"vishal","bangalore"),
            (2,"ajay","villupuram"),
            (4,"dinesh","villupuram"),
            (None,"ganesh","chennai"),
            (2,"ajay","villupuram")]

src_df = spark.createDataFrame(src_data, schema)

# Null IDs
null_df = src_df.filter(col("id").isNull())

# Duplicate IDs
duplicate_ids = src_df.groupBy("id") \
                      .count() \
                      .filter(col("count") > 1) \
                      .filter(col("id").isNotNull()) \
                      .select("id")

duplicate_df = src_df.join(duplicate_ids, "id", "inner")

# Invalid records
invalid_df = null_df.unionByName(duplicate_df)

# Valid records
valid_df = src_df.filter(col("id").isNotNull()) \
                 .dropDuplicates(["id"])

# Remove matching IDs from target
target_remaining = target_df.alias("t").join(
    valid_df.alias("s"),
    col("t.id") == col("s.id"),
    "left_anti"
)

# Final table
final_df = target_remaining.unionByName(valid_df)

final_df.orderBy(col("id").asc()).show()

spark.stop()


'''
SCD1 MERGE (Delta / BigQuery / Snowflake Style)

MERGE INTO target t
USING source s
ON t.id = s.id

WHEN MATCHED THEN
  UPDATE SET
    t.name = s.name,
    t.city = s.city

WHEN NOT MATCHED  THEN
  INSERT (id, name, city)
  VALUES (s.id, s.name, s.city);
 
'''