def extract_data(rows):
    for row in rows:
        yield row

def transform_data(data):
    for record in data:
        record["processed"] = True
        yield record

source="data.csv"
data = transform_data(extract_data(source))

for item in data:
    print(item)