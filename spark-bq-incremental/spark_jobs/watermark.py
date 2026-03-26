from google.cloud import bigquery

client = bigquery.Client()

def get_watermark(table):
    q = f"""
    SELECT COALESCE(MAX(last_watermark), TIMESTAMP('1970-01-01'))
    FROM metadata.watermarks
    WHERE table_name = '{table}'
    """
    return list(client.query(q))[0][0]

def update_watermark(table, watermark):
    client.query(f"""
    INSERT INTO metadata.watermarks(table_name, last_watermark)
    VALUES('{table}', TIMESTAMP('{watermark}'))
    """).result()
