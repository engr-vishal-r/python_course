from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col

# Create SparkSession
spark = SparkSession.builder.appName("salary").getOrCreate()

# Sample data
data = [
    (1, "A", "m", 2500),
    (2, "B", "f", 1500),
    (3, "C", "m", 5500),
    (4, "D", "f", 500)
]

# Create DataFrame with schema
salary = spark.createDataFrame(data, ["id", "name", "sex", "salary"])

# Swap 'm' and 'f' using a single update-like statement
salary = salary["sex"].replace({"m": "f", "f": "m"})

#salary=salary.withColumn("sex", when(col("sex") =="m","f").when(col("sex")=="f","m").otherwise(col("sex")))

salary.show()