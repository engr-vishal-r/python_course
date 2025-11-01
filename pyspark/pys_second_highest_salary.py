from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Create Spark session
spark = SparkSession.builder.getOrCreate()

# Example input
data = [(1, 100), (2, 200), (3, 300)]
employee = spark.createDataFrame(data, ["id", "salary"])

# Find second highest distinct salary
distinct_salaries = employee.select("salary").distinct().orderBy(F.desc("salary"))

# Collect top 2 salaries
top_two = distinct_salaries.limit(2).collect()

# Prepare result
if len(top_two) < 2:
    result = spark.createDataFrame([(None,)], ["SecondHighestSalary"])
else:
    result = spark.createDataFrame([(top_two[1]["salary"],)], ["SecondHighestSalary"])

result.show()