from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lead, lag
from pyspark.sql.window import Window


spark= SparkSession.builder.appName("WindowFunctions").getOrCreate()

json_df=spark.read.json("file:///F:/python_tutorial/pyspark/clean_employees.json")


# 1. Create window spec ordered by salary
window_spec = Window.partitionBy("name").orderBy("joining_date")

# 2. Use lag, lead, datediff without dropping salary
result_df = json_df.withColumn("next_salary", lead("salary", 1).over(window_spec)) \
    .withColumn("prev_salary", lag("salary", 1).over(window_spec)) \
    .withColumn("salary_hike", col("salary") - col("prev_salary"))

# Show selected columns
result_df.select("emp_id", "name", "salary", "prev_salary", "next_salary", "salary_hike").show()