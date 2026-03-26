import pandas as pd

data = [[3, 'Brad', None, 4000], [1, 'John', 3, 1000], [2, 'Dan', 3, 2000], [4, 'Thomas', 3, 4000]]
employee = pd.DataFrame(data, columns=['empId', 'name', 'supervisor', 'salary']).astype({'empId':'Int64', 'name':'object', 'supervisor':'Int64', 'salary':'Int64'})
data = [[2, 500], [4, 2000]]
bonus = pd.DataFrame(data, columns=['empId', 'bonus']).astype({'empId':'Int64', 'bonus':'Int64'})

# Merge
merged = employee.merge(bonus, on="empId", how="left")

# Filter rows where bonus < 1000 OR bonus is null
result = merged[(merged["bonus"].isna()) | (merged["bonus"] < 1000)][["name", "bonus"]]

# Optional: display NaN as 'null' in output
result_display = result.copy().astype({"bonus": "object"})
result_display["bonus"] = result_display["bonus"].where(result_display["bonus"].notna(), 'null')

print(result_display)