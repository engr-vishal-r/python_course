from pyspark.sql import SparkSession
from pyspark.sql.functions import count

spark = SparkSession.builder.appName("act_dir").getOrCreate()

# Input data
data = [
    (1, 1, 0),
    (1, 1, 1),
    (1, 1, 2),
    (1, 2, 3),
    (1, 2, 4),
    (2, 1, 5),
    (2, 1, 6)
]
columns = ["actor_id", "director_id", "timestamp"]

actor_director = spark.createDataFrame(data, columns)

# Group and filter
result = (
    actor_director
    .groupBy("actor_id", "director_id")
    .agg(count("*").alias("count"))
    .filter("count >= 3")
    .select("actor_id", "director_id")
)

# Show final result
result.show()