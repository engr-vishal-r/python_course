from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("ReadMySql") \
    .config("spark.jars", "file:///C:/Users/vishal/drivers/mysql-connector-j-9.4.0/mysql-connector-j-9.4.0.jar") \
    .getOrCreate()
print("spark session created successfully")

#Reading from a mysql Database 
jdbc_url = "jdbc:mysql://localhost:3306/dairydb"
properties = {"user": "root", "password": "root", "driver": "com.mysql.cj.jdbc.Driver"}

mysql_df = spark.read.jdbc(url=jdbc_url, table="product", properties=properties)
mysql_df.show()