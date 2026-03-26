import csv

def extract_data(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield row  # each row is a dict

def transform_data(data):
    for record in data:
        record["processed"] = True
        yield record

source = "F:/python_tutorial/attendance.csv"
data = transform_data(extract_data(source))

for item in data:
    print(item)