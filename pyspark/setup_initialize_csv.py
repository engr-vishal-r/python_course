from pyspark.sql import *
from pyspark.sql.functions import *

spark= SparkSession.builder \
        .appName("ReadCSVFile") \
        .getOrCreate()

print("Spark Session Created Successfully")

read_df=spark.read.csv("file:///F:/E2E_Projects/uber-etl-pipeline-de-project/data/uber_data.csv", header=True,
                        inferSchema=True)

#Rename, Cast Column:
transformed_df = read_df.withColumnRenamed("store_and_fwd_flag", "sf_flag") \
                        .dropna()\
                        .withColumn("total_amount", col("total_amount").cast("Integer"))

# Aggregations and Grouping
agg_df=transformed_df.groupBy("VendorID","sf_flag") \
  .agg(avg("fare_amount").alias("avg_fare_amount"),
       min("fare_amount").alias("min_fare_amount"),
       max("fare_amount").alias("max_fare_amount"),
       sum("fare_amount").alias("total_fare_amount"),
       count("*").alias("num_trips")).show()
"""
agg_df.coalesce(1).write \
.option("header",True) \
.csv("F:/python_tutorial/pyspark/print_vendor_details.csv")
"""