from pyspark.sql import SparkSession
from pyspark.sql.functions import countDistinct
from pyspark.sql.functions import *
from pyspark.sql.window import *

spark = SparkSession.builder.master("local[*]").appName("pyspark_etl_extended").getOrCreate()

# Load DataFrames
emp_df = spark.read.csv("file:///F:/python_tutorial/employee.csv", header=True, inferSchema=True)
sal_df = spark.read.csv("file:///F:/python_tutorial/salary_table.csv", header=True, inferSchema=True)

# NEW CSV — project allocation table
proj_df = spark.read.csv("file:///F:/python_tutorial/project_allocation.csv", header=True, inferSchema=True)
# Columns assumed → empId, projectName, hoursWorked, projectStartDate, projectEndDate

# Replace NULLs
emp_df = emp_df.na.fill(-1)
sal_df = sal_df.na.fill(-1)
proj_df = proj_df.na.fill({"hoursWorked": 0})

# ===========================
# 1) JOIN THREE TABLES
# ===========================
merge_df = (
    emp_df
    .join(sal_df, "empId", "inner")
    .join(proj_df, emp_df.empId==proj_df.employee_Id, "left")  # Keep employee even if no project
)

# Email Pattern
email_pattern = r"[a-z0-9._-]+@[a-z]+\.[a-z]{2,3}$"
# Mobile Pattern
mob_pattern=r"(\+91-)?[0-9]{10}$"

# ===========================
# 2) CLEAN, TRANSFORM
# ===========================
filter_df = (merge_df
    .drop("password")
    .fillna({"bonus": -1})
    .withColumn("email", when(col("email").rlike(email_pattern), col("email")).otherwise("Invalid Email"))\
                .withColumnRenamed("email","email_id")
    .withColumn("age", floor(months_between(current_date(), to_date(col("dob"), "dd-MM-yyyy")) / 12))
    .filter(col("age") >= 18)
    .filter(col("department").isNotNull())
    .withColumn("total_compensation", col("salary") + col("bonus"))
    .withColumn("tax", col("salary") * 0.01)
    .withColumn("service", when(col("is_active") == "Y", "In Service").otherwise("Not In Service"))
    .withColumn("emp_type",
                when((col("yex") >= 10) & (col("yex") <= 12), "Senior")
                .when((col("yex") < 10) & (col("yex") >= 5), "Intermediate")
                .otherwise("Junior"))
    .withColumn("emp_name", upper(concat(col("fname"), lit(" "), col("lname"))))
    .withColumn("phone",concat(lit("+91-"),col("phone")))
)

# ===========================
# 3) WINDOW SPECIFICATIONS
# ===========================
window_rank = Window.partitionBy("department").orderBy(col("salary").desc())
window_cum = window_rank.rowsBetween(Window.unboundedPreceding, Window.currentRow)

# Window for lead, lag, row_number (ordered by project start date)
project_window = Window.partitionBy("empId").orderBy(to_date(col("projectStartDate"), "dd-MM-yyyy"))

# ===========================
# 4) APPLY WINDOW FUNCTIONS
# ===========================
final_df = (filter_df
    .withColumn("cumulative_salary", sum("salary").over(window_cum))
    .withColumn("dense_rank", dense_rank().over(window_rank))
    .withColumn("row_number", row_number().over(project_window))
    .withColumn("lead_project", lead("projectName", 1).over(project_window))
    .withColumn("lag_project", lag("projectName", 1).over(project_window))
    .withColumn("next_project_hours", lead("hoursWorked", 1).over(project_window))
)

# ===========================
# 5) AGGREGATIONS on 3 tables
# ===========================
agg_df = (final_df
    .groupBy("department", "emp_type")
    .agg(
        countDistinct("empId").alias("employee_count"),
        avg("salary").alias("avg_salary"),
        sum("hoursWorked").alias("total_hours_worked"),
        max("total_compensation").alias("max_compensation"),
        min("age").alias("youngest_age")
    )
)

# ===========================
# 6) GET TOP SALARY PER DEPARTMENT
# ===========================
dense_df = final_df.filter(col("dense_rank") == 1)

# SHOW FINAL RESULT
dense_df.select(
    "empId", "emp_name","phone", "email_id", "department", "projectName",
    "salary", "cumulative_salary", "dense_rank",
    "row_number", "lead_project", "lag_project"
).show(truncate=False)

# SHOW AGGREGATION RESULT
agg_df.show(truncate=False)