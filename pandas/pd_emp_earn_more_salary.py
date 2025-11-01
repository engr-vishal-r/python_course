import pandas as pd

# Sample data
data = {
    "id": [1, 2, 3, 4],
    "name": ["Joe", "Henry", "Sam", "Max"],
    "salary": [70000, 80000, 60000, 90000],
    "managerId": [3, 4, None, None]
}

employee = pd.DataFrame(data)

# Self-join: employee with their manager
merged = employee.merge(
    employee,
    left_on="managerId",  # Employee's managerId
    right_on="id",        # Manager's id
    suffixes=("", "_manager")
)

# Filter where employee salary > manager salary
result = merged[merged["salary"] > merged["salary_manager"]][["name"]]

# Rename output column
result.columns = ["Employee"]

print(result)