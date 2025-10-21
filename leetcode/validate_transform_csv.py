import csv
from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

with open('F:/python_tutorial/attendance.csv', 'r') as inp, open('F:/python_tutorial/output.csv', 'w', newline='') as out:
    reader = csv.DictReader(inp)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(out, fieldnames=fieldnames)
    writer.writeheader()
    print("Records updated in the output file")

    for row in reader:
        if validate_date(row['date']):
            row['name'] = row['name'].lower()
            writer.writerow(row)
