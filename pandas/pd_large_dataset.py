import pandas as pd
import numpy as np

# ---------------------------------
# 1️⃣ Create Sample DataFrames
# ---------------------------------
employees = pd.DataFrame({
    'emp_id': [101, 102, 103, 104, 105, 106, 107],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'George'],
    'dept_id': [1, 2, 2, 3, 1, 3, 2],
    'salary': [60000, 75000, 80000, 72000, 62000, 72000, 88000],
    'join_date': pd.to_datetime(['2020-01-15', '2019-05-23', '2021-07-30',
                                 '2020-02-11', '2021-03-19', '2018-11-05', '2023-02-01'])
})

departments = pd.DataFrame({
    'dept_id': [1, 2, 3, 4],
    'dept_name': ['HR', 'IT', 'Finance', 'Admin'],
    'manager': ['John', 'Sara', 'Tom', 'Rachel']
})

projects = pd.DataFrame({
    'proj_id': [201, 202, 203, 204, 205],
    'dept_id': [1, 2, 2, 3, 1],
    'project_name': ['Recruitment', 'Migration', 'AI Model', 'Audit', 'Training']
})

print("📋 Employees Data:")
print(employees, "\n")

# ---------------------------------
# 2️⃣ Joins (Inner, Left, Right, Outer)
# ---------------------------------
# INNER JOIN (only matching dept_id)
inner_join = pd.merge(employees, departments, on='dept_id', how='inner')
print("🤝 INNER JOIN:")
print(inner_join[['emp_id', 'name', 'dept_name', 'manager']], "\n")

# LEFT JOIN
left_join = pd.merge(employees, departments, on='dept_id', how='left')
print("🫱 LEFT JOIN:")
print(left_join[['emp_id', 'name', 'dept_name']], "\n")

# RIGHT JOIN
right_join = pd.merge(employees, departments, on='dept_id', how='right')
print("🫲 RIGHT JOIN:")
print(right_join[['emp_id', 'name', 'dept_name']], "\n")

# FULL OUTER JOIN
outer_join = pd.merge(employees, departments, on='dept_id', how='outer')
print("🌍 FULL OUTER JOIN:")
print(outer_join[['emp_id', 'name', 'dept_name']], "\n")

# ---------------------------------
# 3️⃣ Aggregations & Distinct Counts
# ---------------------------------
agg_df = employees.groupby('dept_id').agg(
    avg_salary=('salary', 'mean'),
    max_salary=('salary', 'max'),
    min_salary=('salary', 'min'),
    total_employees=('emp_id', 'count'),
    distinct_salary_count=('salary', 'nunique')
).reset_index()

print("📈 Aggregations by Department:")
print(agg_df, "\n")

# ---------------------------------
# 4️⃣ Window Functions
# ---------------------------------
from pandas import DataFrame

# RANK(), DENSE_RANK(), ROW_NUMBER()
employees['rank_salary'] = employees['salary'].rank(method='average', ascending=False)
employees['dense_rank_salary'] = employees['salary'].rank(method='dense', ascending=False)
employees['row_number'] = employees.sort_values(['dept_id', 'salary'], ascending=[True, False]) \
    .groupby('dept_id') \
    .cumcount() + 1

print("🏆 Window Functions (Rank, Dense Rank, Row Number):")
print(employees[['emp_id', 'name', 'dept_id', 'salary', 'rank_salary', 'dense_rank_salary', 'row_number']], "\n")

# ROLLING window example: 3-period moving average of salary (sorted by join_date)
employees = employees.sort_values('join_date')
employees['rolling_avg_salary'] = employees['salary'].rolling(window=3, min_periods=1).mean()
print("📊 Rolling Average of Salary (last 3 employees):")
print(employees[['emp_id', 'name', 'join_date', 'salary', 'rolling_avg_salary']], "\n")

# ---------------------------------
# 5️⃣ Combining Data (Joins + Aggregations)
# ---------------------------------
# Join departments and employees to see department-wise metrics
dept_summary = pd.merge(employees, departments, on='dept_id', how='left')
dept_summary = dept_summary.groupby(['dept_name']).agg(
    total_salary=('salary', 'sum'),
    avg_salary=('salary', 'mean'),
    employee_count=('emp_id', 'count')
).reset_index()

print("🏢 Department Summary (Join + Aggregate):")
print(dept_summary, "\n")

# ---------------------------------
# 6️⃣ Multi-level GroupBy (Dept + Year)
# ---------------------------------
employees['join_year'] = employees['join_date'].dt.year
yearly_stats = employees.groupby(['dept_id', 'join_year']).agg(
    emp_count=('emp_id', 'count'),
    avg_salary=('salary', 'mean')
).reset_index()

print("📅 Multi-level GroupBy (Dept + Join Year):")
print(yearly_stats, "\n")

# ---------------------------------
# 7️⃣ Distinct count check with nunique()
# ---------------------------------
distinct_names = employees['name'].nunique()
print(f"🧍‍♂️ Distinct Employee Names Count: {distinct_names}\n")

# ---------------------------------
# 8️⃣ Advanced Example: Top 2 Salaries per Department (using window)
# ---------------------------------
top2 = employees.sort_values(['dept_id', 'salary'], ascending=[True, False]) \
    .groupby('dept_id').head(2)

print("🥇 Top 2 Salaries per Department:")
print(top2[['dept_id', 'name', 'salary']], "\n")

# ---------------------------------
# 9️⃣ Join Projects Table (1-to-many)
# ---------------------------------
emp_proj = pd.merge(employees, projects, on='dept_id', how='left')
print("🚀 Employee - Project Join:")
print(emp_proj[['name', 'dept_id', 'project_name']], "\n")

# ---------------------------------
# 🔟 Export Final Data
# ---------------------------------
emp_proj.to_csv("F:/python_tutorial/pandas/final_pandas_operations.csv", index=False)
print("✅ Exported final combined dataset: 'final_pandas_operations.csv'")