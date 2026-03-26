import json
from pathlib import Path
import pandas as pd

input_file=Path(r"F:/python_tutorial/pyspark/clean_employees.json")
with open(input_file) as raw_data:

    flat_data = []

    for line in raw_data:
        emp=json.loads(line)

        father = None
        mother = None

        for parent in emp.get("parents",[]):
            name = parent.get("name") or "NA"
            if parent.get("name") is not None and parent.get("relation") == "Father":
                father = name
            elif  parent.get("name") is not None and parent.get("relation") == "Mother":
                mother = name

        for addr in emp.get("addresses", []):

            comm = addr.get("communication_address", {})
            perm = addr.get("permanent_address", {})

            flat_data.append({
            "emp_id": emp["emp_id"],
            "name": emp["name"],
            "full_name":emp["name"] + " " + (father or "NA"),

            "comm_area": comm.get("area"),
            "perm_area": perm.get("area")
        })
df=pd.DataFrame(flat_data)
print(df.to_string(index=False))
output_df=input_file.parent / f"{input_file.stem}_formatted.json"
with open(output_df,"w") as f:
    json.dump(flat_data, f, indent=4)

print("File written to:", output_df)