from pyspark.sql import SparkSession
from pyspark.sql.functions import col, broadcast

spark = SparkSession.builder.appName("pyspark_cdc_incremental").getOrCreate()

# Target data
target_data = [(1,"vishal","chennai"),
            (2,"ajay","villupuram"),
            (3,"ramesh","vellore")]
target_col = ["id","name","city"]

target_df = spark.createDataFrame(target_data, target_col)

# CDC data
cdc_data = [(1,"vishal","bangalore","U"),
            (2,"ajay","villupuram","D"),
            (4,"dinesh","villupuram","I")]
cdc_col = ["id","name","city","op"]

cdc_df = spark.createDataFrame(cdc_data, cdc_col)

# Separate CDC types
delete_df = cdc_df.filter(col("op") == "D").select("id")
update_df = cdc_df.filter(col("op") == "U").drop("op")
insert_df = cdc_df.filter(col("op") == "I").drop("op")

# 1️⃣ Apply Deletes (remove rows from target)
after_delete_df = target_df.join(broadcast(delete_df), "id", "left_anti")

# 2️⃣ Apply Updates (remove old rows + add updated rows)
after_update_df = after_delete_df.join(broadcast(update_df).select("id"), "id", "left_anti") \
    .unionByName(update_df)

# 3️⃣ Apply Inserts (add new rows)
final_df = after_update_df.unionByName(insert_df)

final_df.orderBy(col("id").asc()).show()

'''
CDC MERGE (Delta / BigQuery / Snowflake Style)

MERGE INTO target t
USING cdc s
ON t.id = s.id

WHEN MATCHED AND s.op = 'D' THEN
  DELETE

WHEN MATCHED AND s.op = 'U' THEN
  UPDATE SET
    t.name = s.name,
    t.city = s.city

WHEN NOT MATCHED AND s.op = 'I' THEN
  INSERT (id, name, city)
  VALUES (s.id, s.name, s.city);
 
'''