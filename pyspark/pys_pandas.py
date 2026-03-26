import pandas as pd
import numpy as np
from datetime import datetime

'''
pd_emp_df=pd.read_csv("file:///F:/python_tutorial/pyspark/employee.csv")
pd_sal_df=pd.read_csv("file:///F:/python_tutorial/pyspark/salary_table.csv")


pattern=r"^[a-z0-9._-]+@[a-z]+\.(com|org|in|co)$"
pd_df=pd.merge(pd_emp_df, pd_sal_df, left_on='empId',right_on='salary_id')

pd_df = (
    pd_df.assign(
        emp_type=lambda df: np.where(df["yex"] > 2, "Perm", "Temp"),
        full_name=lambda df: df["fname"] + " " + df["lname"],
        email=lambda df: np.where(df["email"].str.match(pattern, case=False, na=False), df["email"], "NA"),
        age=lambda df: datetime.now().year - pd.to_datetime(df["dob"], errors="coerce").dt.year,
        is_adult=lambda df: np.where(df["age"] >= 18, "adult", "kid")
    )
)


print(pd_df[["full_name","emp_type","email","is_adult"]])

'''

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark=SparkSession.builder.master("local[*]").appName("demo").getOrCreate()


emp_df=spark.read.csv("file:///F:/python_tutorial/pyspark/employee.csv", header=True, inferSchema=True)
sal_df=spark.read.csv("file:///F:/python_tutorial/pyspark/salary_table.csv", header=True, inferSchema=True)

pattern=r"^[a-z0-9._-]+@[a-z]+\.(com|co|org|in)$"
merged= (emp_df.join(sal_df, emp_df.empId == sal_df.salary_id, "inner")
        .withColumn("emp_type", when(col("yex") > 2, "Perm").otherwise("Temp"))
        .withColumn("full_name",concat(col("fname"),lit(" "),col("lname")))
        .withColumn("full_name", upper(col("full_name")))
        .withColumn("age",floor(months_between(current_date(), col("dob")) / 12))
        .withColumn("is_adult",when(col("age") >=18, "Yes").otherwise("No"))
        .withColumn("email",when(col("email").rlike(pattern), col("email")).otherwise("NA"))
        .select("emp_type","full_name","is_adult","email")
         )

merged.show(truncate=False)