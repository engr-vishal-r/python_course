import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="root",
        database="dairydb"
    )
print("✅ Connected to MySQL")

df_sql = pd.read_sql_query("SELECT * FROM dairydb.customer", conn)
print(df_sql)
conn.close()