from pyspark.sql import SparkSession

spark= SparkSession.builder.appName("test").getOrCreate()

data = [("John", 28), ("Alice", 34)]
columns = ["Name", "Age"]

sdf=spark.createDataFrame(data,schema=columns)

sdf.show()