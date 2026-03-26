from pyspark.sql import SparkSession
from pyspark.sql.functions import posexplode, monotonically_increasing_id, first

# Create Spark session
spark = SparkSession.builder.appName("explode_array").getOrCreate()

# Sample data
data = [
    (["a1","a2","a3"],),
    (["b1","b2","b3"],),
    (["c1","c2","c3"],)
]

df = spark.createDataFrame(data, ["array_col"])

# Step 1: Add unique row id
df_with_id = df.withColumn("id", monotonically_increasing_id())

# Step 2: Explode with position
exploded_df = df_with_id.select("id", posexplode("array_col").alias("pos", "val"))

# Step 3: Pivot
pivot_df = exploded_df.groupBy("id").pivot("pos").agg(first("val"))

# Step 4: Rename columns
result_df = pivot_df.selectExpr(
    "`0` as A",
    "`1` as B",
    "`2` as C"
)

'''
#simpler way for fixed columns
df.select(
    col("array_col")[0].alias("A"),
    col("array_col")[1].alias("B"),
    col("array_col")[2].alias("C")
).show()
'''

# Show result
result_df.show()