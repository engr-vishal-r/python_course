from google.cloud import bigquery
from pyspark.sql.functions import lit
import pandas as pd


def write_errors(df, table, error_type="INVALID_DATA"):
    client = bigquery.Client()

    pdf = (
        df
        .withColumn("table_name", lit(table))
        .withColumn("error_type", lit(error_type))
        .toPandas()
    )

    client.load_table_from_dataframe(
        pdf,
        "metadata.spark_errors"
    ).result()