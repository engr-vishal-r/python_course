from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import *

spark= SparkSession.builder.appName("sample").getOrCreate()

input_df=spark.read.csv("F:\python_tutorial\pandas\monthly_sales.csv",inferSchema=True,header=True)

window=Window.partitionBy("DealershipID","Month").orderBy(col("Sales_Amount").desc())

rnk=input_df.withColumn("rnk",row_number().over(window)).filter(col("rnk")==1).drop("rnk")

top_monthly_performer=rnk.groupBy("DealershipID","EmployeeID").agg(count("*").alias("MonthsAsTopSeller"))

window2=Window.partitionBy("DealershipID").orderBy(col("MonthsAsTopSeller").desc())

top_performer=top_monthly_performer.withColumn("top_rnk",row_number().over(window2)).filter(col("top_rnk")==1).drop("top_rnk")

top_performer.show()

cum_sales=input_df.groupBy("DealershipID").agg(sum("Sales_Amount").alias("Sales_Amount")).orderBy(col("Sales_Amount").desc())

cum_sales.show()