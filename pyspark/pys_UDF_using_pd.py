from pyspark.sql.functions import pandas_udf
from pyspark.sql.types import DoubleType
import pandas as pd
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("UDF Example").getOrCreate()

@pandas_udf(DoubleType())
def multiple_10x(s :pd.Series) -> pd.Series:
    return s * 10
df = spark.createDataFrame([(1,), (2,), (3,)], ["num"])
df.withColumn("num_x10", multiple_10x("num")).show()