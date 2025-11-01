import pandas as pd

def nth_high_salary(data : pd.DataFrame) -> pd.DataFrame:
    sorted_data=data.sort_values(by='salary',ascending=False).fillna(0)[["id","salary","managerId"]]
    sorted_data["managerId"]=sorted_data["managerId"].astype(int)

    return sorted_data



data = pd.DataFrame({
    "id": [1, 2, 3, 4,5],
    "name": ["Joe", "Henry", "Sam", "Max","Henry"],
    "salary": [70000, 80000, 60000, 90000,110000],
    "managerId": [3, 4, None, None, None]
})

print(nth_high_salary(data))