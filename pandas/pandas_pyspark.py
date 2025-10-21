import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import collect_set, max,min,datediff, col, dense_rank,row_number, rank,current_date, months_between, floor, to_date
from pyspark.sql.window import Window

spark= SparkSession.builder \
        .appName("ReadJson")\
        .getOrCreate()

json_df=spark.read.json("file:///F:/python_tutorial/pyspark/clean_employees.json")

# Filtering in pyspark
json_df = json_df.filter((col("dept_id") >= 1) & (col("salary") > 50000))
# Group by dept_id and get unique names as set/list in pyspark
clean_df=json_df.dropna()
clean_df.groupBy("dept_id").agg(collect_set("name").alias("unique_names")).orderBy("dept_id").show(truncate=False)

pandas_df=pd.read_json("file:///F:/python_tutorial/pyspark/employees.json") 
# Filtering in pandas
pandas_df=(pandas_df[(pandas_df['dept_id'] >= 1) & (pandas_df['salary'] > 50000)])
# Group by dept_id and get unique names as set/list in pandas
pandas_df = pandas_df.dropna(subset=["dept_id"])
pandas_df["dept_id"] = pandas_df["dept_id"].astype(int)
print(pandas_df.groupby("dept_id")["name"].apply(lambda names: list(dict.fromkeys(names))).reset_index(name="unique_names").sort_values(by="dept_id").to_string(index=False))

#pyspark
# Step 1: Convert joining_date to datetime
df = clean_df.withColumn("joining_date", col("joining_date").cast("date"))
# Step 2: Group by name and get max/min hire dates
agg_df=df.groupBy("name").agg(
    max("joining_date").alias("latest_hire"),
    min("joining_date").alias("first_hire"))
# Step 3: Calculate days between hires
result_df=agg_df.withColumn("days_diff_btwn_hires",datediff("latest_hire","first_hire"))
# show selected columns in pyspark
result_df.select('name','first_hire','latest_hire','days_diff_btwn_hires').show()

#pandas
# Step 1: Convert joining_date to datetime
pandas_df['joining_date'] = pd.to_datetime(pandas_df['joining_date'], errors='coerce')
# Step 2: Group by name and get max/min hire dates
agg_df = pandas_df.groupby('name').agg(
    latest_hire=('joining_date', 'max'),
    first_hire=('joining_date', 'min')
).reset_index()
# Step 3: Calculate days between hires
agg_df['days_between_hires'] = (agg_df['latest_hire'] - agg_df['first_hire']).dt.days
# Step 4: View result
print(agg_df.to_string(index=False))

#pyspark
# Read Excel files by converting to CSV first or using spark-excel library (assumed CSV here)
emp_df = spark.read.csv("file:///F:/python_tutorial/pyspark/employee.csv", header=True, inferSchema=True)
sal_df = spark.read.csv("file:///F:/python_tutorial/pyspark/salary_table.csv", header=True, inferSchema=True)

sal_df = sal_df.fillna({"salary": -1})
sal_df = sal_df.withColumn("salary", col("salary").cast("int"))
# Join DataFrames
joined_df = emp_df.join(sal_df, emp_df.empId == sal_df.salary_id, "inner")
# Create window spec
windowSpec = Window.orderBy(col("salary").desc())
# Apply dense_rank
ranked_df = joined_df.withColumn("rank_salary", dense_rank().over(windowSpec))
# Filter where rank_salary == 2
result_df = ranked_df.filter(col("rank_salary") == 2).select("empId", "fname", "salary").distinct()
# Show result
result_df.show(truncate=False)

#pandas
pd_emp_df=pd.read_csv("file:///F:/python_tutorial/pyspark/employee.csv")
pd_sal_df=pd.read_csv("file:///F:/python_tutorial/pyspark/salary_table.csv")

# Merge on empId and salary_id
pd_sal_df["salary"] = pd_sal_df["salary"].fillna(-1).astype(int)
merged_df = pd.merge(pd_emp_df, pd_sal_df, left_on="empId", right_on="salary_id")
# Rank salaries using dense rank
merged_df["rank_salary"] = merged_df["salary"].rank(method="dense", ascending=False)
# Filter only rows with rank_salary == 2
filtered_df = merged_df[merged_df["rank_salary"] == 2][["empId", "fname", "salary"]].drop_duplicates()
print(filtered_df.to_string(index=False))

#pyspark
emp_df = emp_df.withColumn("age", to_date(col("dob"), "dd-MM-yyyy"))
emp_df = emp_df.withColumn(
    "age", 
    floor(months_between(current_date(), col("age")) / 12)
)
employee_df_18plus = emp_df.filter(col("age") >= 18)
employee_df_18plus.show()

#pandas
pd_emp_df["dob"] = pd.to_datetime(pd_emp_df["dob"], format="%d-%m-%Y", errors='coerce')
pd_emp_df["phone"]= pd_emp_df["phone"].astype(str)
# Calculate age
today = pd.to_datetime("today")
pd_emp_df["age"] = (today - pd_emp_df["dob"]).dt.days // 365
# Filter employees aged 18 or more
emp_pd_df_18plus = pd_emp_df[pd_emp_df["age"] >= 18]
print(emp_pd_df_18plus.to_string(index=False))

#SQL
emp_df=emp_df.withColumn("dob", to_date(col("dob"), "dd-MM-yyyy"))
emp_df.createOrReplaceTempView("employees")
result = spark.sql("SELECT  *, FLOOR(months_between(current_date(), dob) / 12) AS age FROM employees WHERE FLOOR(months_between(current_date(), dob) / 12) >= 18")
result.show()