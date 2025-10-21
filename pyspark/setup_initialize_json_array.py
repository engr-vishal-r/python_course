from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder.appName("ReadJsonArray").getOrCreate()

# Step 1: Read the entire file as a single string
employees_df = spark.read.text("file:///F:/python_tutorial/pyspark/employees.json") 
dept_df = spark.read.text("file:///F:/python_tutorial/pyspark/departments.json")

# Step 2: Define schemas
emp_schema = StructType([
    StructField("emp_id", IntegerType()),
    StructField("name", StringType()),
    StructField("salary", IntegerType()),
    StructField("dept_id", IntegerType()),
    StructField("joining_date", StringType())
])

dept_schema = StructType([
    StructField("dept_id", IntegerType()),
    StructField("subject", StringType())
])

# Step 3: Parse JSON
json_emp_df = employees_df.select(from_json(employees_df.value, ArrayType(emp_schema)).alias("data"))
json_dept_df = dept_df.select(from_json(dept_df.value, ArrayType(dept_schema)).alias("data"))

# Step 4: Explode arrays
final_emp_df = json_emp_df.select(explode("data").alias("item"))
final_dept_df = json_dept_df.select(explode("data").alias("item"))

# Step 5: Flatten
flattened_emp_df = final_emp_df.select("item.*")
flattened_dept_df = final_dept_df.select("item.*")

# Step 6: Clean & Filter
clean_df = flattened_emp_df.dropna().filter(flattened_emp_df['salary'] > 30000)

# Step 7: Join
joined_df = clean_df.join(flattened_dept_df, on="dept_id", how="inner")

# Final Output
joined_df.select("name", "subject", "salary").show()

#Write to Parquet / JSON / CSV
#joined_df.write.mode("overwrite").parquet("file:///F:/python_tutorial/pyspark/joined_data.parquet")

# Convert 'joining_date' column to date type if needed
df = flattened_emp_df.withColumn("joining_date", to_date("joining_date"))

# Group by name and calculate max, min, and date difference
agg_df = df.groupBy("name").agg(
    max("joining_date").alias("latest_hire"),
    min("joining_date").alias("first_hire")
)

# Add days_between_hires column
result_df = agg_df.withColumn(
    "days_between_hires",
    datediff("latest_hire", "first_hire")
)

# show result
result_df.show()