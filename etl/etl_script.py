import pymysql
import pandas as pd
from datetime import datetime
from confluent_kafka import Producer
import os

p = Producer({'bootstrap.servers': '172.17.22.218:9092'})

def delivery_report(err, msg):
    if err is not None:
        print('Delivery failed:', err)
    else:
        print('Message delivered to', msg.topic(), msg.partition())

def fetch_data_from_mysql():
    mysql_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'etl_example'
    }

    connection = pymysql.connect(**mysql_config)
    query = 'SELECT * FROM customer_data'
    df = pd.read_sql(query, connection)
    print('Connected to database successfully!!')
    connection.close()
    return df

def transform_data(df):
    df_transformed = df[df['age'] < 30]
    print('Data successfully fetched from Database!!')
    return df_transformed

def write_data_to_file(df):
    output_dir = 'F:/python_tutorial/extract'
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = f'etl_output_{timestamp}.csv'
    file_path = os.path.join(output_dir, file_name)
    df.to_csv(file_path, index=False)
    print(f'Data written to {file_path}')

def send_to_kafka(df):
    for _, row in df.iterrows():
        message = row.to_json()
        p.produce('kafka_topic_vb', key=str(row['id']), value=message, callback=delivery_report)
        print('Messages published successfully!!')
    p.flush()

def etl_process():
    df = fetch_data_from_mysql()
    df_transformed = transform_data(df)
    write_data_to_file(df_transformed)
    send_to_kafka(df_transformed)

if __name__ == "__main__":
    etl_process()