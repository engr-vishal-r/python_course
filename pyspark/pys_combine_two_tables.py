from pyspark.sql import SparkSession

# Initialize Spark
spark = SparkSession.builder.appName("JoinExample").getOrCreate()

# Create DataFrames
person_data = [
    (1, "Wang", "Allen"),
    (2, "Alice", "Bob")
]
address_data = [
    (1, 2, "New York City", "New York"),
    (2, 3, "Leetcode", "California")
]

person_columns = ["personId", "lastName", "firstName"]
address_columns = ["addressId", "personId", "city", "state"]

person_df = spark.createDataFrame(person_data, person_columns)
address_df = spark.createDataFrame(address_data, address_columns)

# LEFT JOIN on personId
result_df = person_df.join(address_df, on="personId", how="left")\
    .select("firstName", "lastName", "city", "state")

result_df.show()