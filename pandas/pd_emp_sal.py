import pandas as pd
import numpy as np
from datetime import datetime

emp_df=pd.read_csv("file:///F:/python_tutorial/employee.csv")
sal_df=pd.read_csv("file:///F:/python_tutorial/salary_table.csv")


emp_df=emp_df.fillna(-1)
sal_df=sal_df.fillna(-1)

merged_df=pd.merge(emp_df, sal_df, left_on="empId",right_on="empId",how="inner")

merged_df=merged_df.drop(["password","phone"], axis=1)

pattern=r"[a-z0-9._-]+@[a-z]+\.(co|com|org|in)$"

filtered_df = (
    merged_df
    .assign(
        email=lambda x: np.where(
            x["email"].astype(str).str.lower().str.match(pattern, na=False),
            x["email"],
            "Invalid Email"
        ),
        age=lambda x: datetime.now().year - pd.to_datetime(
            x["dob"], format="%d-%m-%Y", errors="coerce"
        ).dt.year,
        total_compensation=lambda x: x["salary"] + x["bonus"],
        tax=lambda x: x["salary"] * 0.1,
        service_type=lambda x: np.where(
            x["is_active"] == 'Y', "In service", "Not In Service"
        ),
        emp_type=lambda x: np.where(
            (x["yex"] >= 10) & (x["yex"] <= 12),
            "Senior",
            np.where(
                (x["yex"] < 10) & (x["yex"] >= 5),
                "Intermediate",
                "Junior"
            )
        )
       
    )
    .loc[lambda x: (x["age"] >= 18) & (x["department"].notna())]
)

filtered_df["emp_name"]=filtered_df["fname"]+" "+filtered_df["lname"]
filtered_df["emp_name"]=filtered_df["emp_name"].str.upper()
filtered_df=filtered_df.rename(columns={"email":"email_id"})

print(filtered_df[["emp_name","salary","email_id","department","dob","yex","age","total_compensation","is_active","emp_type"]])