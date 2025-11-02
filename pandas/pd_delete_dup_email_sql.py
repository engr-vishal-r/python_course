import pandas as pd
import mysql.connector

conn=mysql.connector.connect(
    host="localhost",\
    port=3306,\
    user="root",\
    password="root",\
    database="employee_db"
)

cursor = conn.cursor()

delete_query = """DELETE FROM Person WHERE id NOT IN (SELECT * FROM (SELECT min(id) FROM Person GROUP BY email) As Temp);"""

cursor.execute(delete_query)
conn.commit()

df_sql=pd.read_sql_query("SELECT * FROM Person;", conn)

print(df_sql)

cursor.close()
conn.close()