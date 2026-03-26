from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName("UDF Example").getOrCreate()

# Sample data
data = [("vishal",), ("arjun",), ("sanjay",)]
df = spark.createDataFrame(data, ["name"])

# Step 1: Define a Python function
def upper_case(name):
    return name.upper()

# Step 2: Register as a UDF
upper_udf = udf(upper_case, StringType())

# Step 3: Use in DataFrame
df.withColumn("upper_name", upper_udf(df["name"])).show()