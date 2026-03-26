from pyspark.sql.types import (
    StructType, StructField,
    StringType, IntegerType,
    TimestampType, DoubleType
)


def get_schema(table_name: str):

    if table_name == "transactions":
        return StructType([
            StructField("id", StringType(), True),
            StructField("amount", DoubleType(), True),
            StructField("updated_at", TimestampType(), True)
        ])

    elif table_name == "customers":
        return StructType([
            StructField("id", StringType(), True),
            StructField("name", StringType(), True),
            StructField("city", StringType(), True),
            StructField("updated_at", TimestampType(), True)
        ])

    else:
        raise ValueError(f"No schema defined for {table_name}")