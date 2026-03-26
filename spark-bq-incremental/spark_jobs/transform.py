from pyspark.sql.functions import when, col, trim
from utils.udf_utils import categorize_amount_udf


def transform(df, spark):

    # -------------------------
    # Primary Key Validation
    # -------------------------
    invalid_pk_df = df.filter(
        col("id").isNull() |
        (trim(col("id")) == "")
    )

    # -------------------------
    # Valid Rows
    # -------------------------
    valid_df = df.filter(
        col("id").isNotNull() &
        (trim(col("id")) != "")
    )

    # Business transformation
    good_df = (
        valid_df
        .withColumn(
            "amount",
            when(col("amount").isNull(), 0)
            .otherwise(col("amount"))
        )
        .withColumn(
            "amount_category",
            categorize_amount_udf(col("amount"))
        )
    )

    return good_df, invalid_pk_df