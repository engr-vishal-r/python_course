import csv
from pathlib import Path

input_path = Path(r"F:\python_tutorial\pandas\hire_summary.csv")
output_path = input_path.parent / f"{input_path.stem}_output_hire.csv"

with open(input_path, "r") as input_df, open(output_path, "w", newline="") as output_df:

    reader = csv.DictReader(input_df)

    fieldnames = reader.fieldnames + ["level"]   # add new column

    writer = csv.DictWriter(output_df, fieldnames=fieldnames)

    writer.writeheader()

    for row in reader:
        if int(row["days_between_hires"]) >= 400:
            row["level"] = "Senior"
        else:
            row["level"] = "Junior"

        writer.writerow(row)