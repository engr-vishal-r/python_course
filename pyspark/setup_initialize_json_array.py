from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col, to_date, max, min, datediff

# ---------------------------------------------------------
# 1. Create Spark Session
# ---------------------------------------------------------

spark = SparkSession.builder \
    .appName("Employee JSON Processing") \
    .getOrCreate()


# ---------------------------------------------------------
# 2. Read JSON Files
# ---------------------------------------------------------

emp_df = spark.read.json("file:///F:/python_tutorial/pyspark/employees.json")
dept_df = spark.read.json("file:///F:/python_tutorial/pyspark/departments.json")


# ---------------------------------------------------------
# 3. Flatten Nested JSON (addresses)
# ---------------------------------------------------------

emp_flat_df = emp_df \
    .withColumn("address", explode("addresses")) \
    .select(
        "emp_id",
        "name",
        "salary",
        "dept_id",
        "joining_date",
        col("address.communication_address.area").alias("area")
    )


# ---------------------------------------------------------
# 4. Clean Data
# ---------------------------------------------------------

clean_df = emp_flat_df \
    .dropna() \
    .filter(col("salary") > 30000)


# ---------------------------------------------------------
# 5. Join with Department Table
# ---------------------------------------------------------

joined_df = clean_df.join(
    dept_df,
    on="dept_id",
    how="inner"
)


# ---------------------------------------------------------
# 6. Show Final Employee Output
# ---------------------------------------------------------

print("Employee Details After Join")

joined_df.select(
    "name",
    "subject",
    "salary",
    "area"
).show(truncate=False)


# ---------------------------------------------------------
# 7. Convert Joining Date to Date Type
# ---------------------------------------------------------

date_df = emp_flat_df.withColumn(
    "joining_date",
    to_date("joining_date")
)


# ---------------------------------------------------------
# 8. Aggregation
# Find earliest and latest joining per employee
# ---------------------------------------------------------

agg_df = date_df.groupBy("name").agg(
    max("joining_date").alias("latest_hire"),
    min("joining_date").alias("first_hire")
)


# ---------------------------------------------------------
# 9. Calculate Days Between Hires
# ---------------------------------------------------------

result_df = agg_df.withColumn(
    "days_between_hires",
    datediff(col("latest_hire"), col("first_hire"))
)


# ---------------------------------------------------------
# 10. Show Aggregated Results
# ---------------------------------------------------------

print("Employee Hire Gap Analysis")

result_df.show(truncate=False)


# ---------------------------------------------------------
# 11. Stop Spark Session
# ---------------------------------------------------------

spark.stop()