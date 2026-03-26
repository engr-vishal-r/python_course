from pyspark.sql.functions import udf
from pyspark.sql.types import StringType


# Business Logic
def categorize_amount(amount):
    if amount is None:
        return "UNKNOWN"
    elif amount <= 100:
        return "LOW"
    elif amount <= 1000:
        return "MEDIUM"
    else:
        return "HIGH"


# DataFrame API usage
categorize_amount_udf = udf(categorize_amount, StringType())


# SQL usage
def register_udfs(spark):
    spark.udf.register(
        "categorize_amount",
        categorize_amount,
        StringType()
    )