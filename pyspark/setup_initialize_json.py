from pyspark.sql import SparkSession
from pyspark.sql.functions import collect_set, max,min,datediff, col, explode, expr

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


df_flat = df.withColumn("addr", explode("addresses")).select(
    "emp_id",
    "name",
    col("addr.communication_address.door_no").alias("comm_door_no"),
    col("addr.communication_address.street").alias("comm_street"),
    col("addr.communication_address.area").alias("comm_area"),
    col("addr.permanent_address.door_no").alias("perm_door_no"),
    col("addr.permanent_address.street").alias("perm_street"),
    col("addr.permanent_address.area").alias("perm_area"),
    expr("filter(parents, x -> x.relation = 'Father')[0].name").alias("father"),
    expr("filter(parents, x -> x.relation = 'Mother')[0].name").alias("mother")
)

df_flat.show()


#df_flat.write.format("delta").mode("overwrite").save("silver/employee")
# show selected columns
#result_df.select('name','first_hire','latest_hire','days_diff_btwn_hires').show()
#final_df.write.mode("overwrite").parquet("file:///F:/python_tutorial/pyspark/output_parquet")