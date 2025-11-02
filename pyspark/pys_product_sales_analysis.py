from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ProductSales").getOrCreate()

# Create Sales DataFrame
sales_data = [
    (1, 100, 2008, 10, 5000),
    (2, 100, 2009, 12, 5000),
    (7, 200, 2011, 15, 9000)
]
sales_columns = ["sale_id", "product_id", "year", "quantity", "price"]
sales_df = spark.createDataFrame(sales_data, sales_columns)

# Create Product DataFrame
product_data = [
    (100, "Nokia"),
    (200, "Apple"),
    (300, "Samsung")
]
product_columns = ["product_id", "product_name"]
product_df = spark.createDataFrame(product_data, product_columns)

# Join and select required columns
result_df = sales_df.join(product_df, on="product_id", how="inner") \
                    .select("product_name", "year", "price")

result_df.show()