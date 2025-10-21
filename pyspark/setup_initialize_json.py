from pyspark.sql import SparkSession
from pyspark.sql.functions import collect_set, max,min,datediff, col

spark= SparkSession.builder \
        .appName("ReadJson")\
        .getOrCreate()

json_df=spark.read.json("file:///F:/python_tutorial/pyspark/clean_employees.json") 

json_df.groupBy("dept_id").agg(collect_set("name").alias("unique_names")).show()

# Convert 'joining_date' column to date type if needed
df = json_df.withColumn("joining_date", col("joining_date").cast("date"))

agg_df=df.groupBy("name").agg(
    max("joining_date").alias("latest_hire"),
    min("joining_date").alias("first_hire"))

result_df=agg_df.withColumn("days_diff_btwn_hires",datediff("latest_hire","first_hire"))

# show selected columns
result_df.select('name','first_hire','latest_hire','days_diff_btwn_hires').show()
#final_df.write.mode("overwrite").parquet("file:///F:/python_tutorial/pyspark/output_parquet")