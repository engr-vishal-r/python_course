from pyspark.sql import SparkSession
from pyspark.sql.functions import col


spark=SparkSession.builder.appName("delDup").getOrCreate()

person=[(1,"abc@gmail.com"),(2,"gmail@gmail.com"),(3,"abc@gmail.com")]

person_column=["id","email"]

person_df=spark.createDataFrame(person,person_column)

sorted_person=person_df.orderBy(col("id").asc())

result=sorted_person.dropDuplicates(["email"])

result.show()