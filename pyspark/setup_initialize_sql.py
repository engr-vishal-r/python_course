from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("ReadMySql") \
    .config("spark.jars", "file:///C:/Users/vishal/drivers/mysql-connector-j-9.4.0/mysql-connector-j-9.4.0.jar") \
    .getOrCreate()
print("spark session created successfully")

#Reading from a mysql Database 
jdbc_url = "jdbc:mysql://localhost:3306/dairydb"
properties = {"user": "root", "password": "root", "driver": "com.mysql.cj.jdbc.Driver"}

# Read MySQL table with partitioning
mysql_df = (
    spark.read
    .format("jdbc")
    .option("url", jdbc_url)
    .option("dbtable", "product")
    .option("partitionColumn", "card_number")
    .option("lowerBound", 1)
    .option("upperBound", 100000000)
    .option("numPartitions", 4)
    .options(**properties)
    .load()
)
mysql_df.show()