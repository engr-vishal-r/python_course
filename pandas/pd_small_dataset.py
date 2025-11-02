import pandas as pd
import numpy as np

# -------------------------------
# 1️⃣ Create sample DataFrames
# -------------------------------
employees = pd.DataFrame({
    'emp_id': [101, 102, 103, 104, 105, 106],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'dept': ['HR', 'IT', 'IT', 'Finance', 'HR', 'Finance'],
    'salary': [60000, 75000, 80000, np.nan, 62000, 72000],
    'join_date': pd.to_datetime(['2020-01-15', '2019-05-23', '2021-07-30', '2020-02-11', '2021-03-19', '2018-11-05'])
})

departments = pd.DataFrame({
    'dept': ['HR', 'IT', 'Finance', 'Admin'],
    'manager': ['John', 'Sara', 'Tom', 'Rachel']
})

print("📋 Original Employees Data:")
print(employees, "\n")

# -------------------------------
# 2️⃣ Basic selection & filtering
# -------------------------------
print("🔍 Employees in IT Department:")
print(employees[employees['dept'] == 'IT'], "\n")

# Select specific columns
print("🎯 Names and Salaries:")
print(employees[['name', 'salary']], "\n")

# -------------------------------
# 3️⃣ Sorting data
# -------------------------------
print("📊 Sorted by Salary (descending):")
print(employees.sort_values(by='salary', ascending=False), "\n")

# -------------------------------
# 4️⃣ Add / update columns
# -------------------------------
employees['bonus'] = employees['salary'] * 0.10
employees['year_joined'] = employees['join_date'].dt.year
print("💰 Added Bonus and Year Joined Columns:")
print(employees, "\n")

# -------------------------------
# 5️⃣ Handle missing values
# -------------------------------
employees['salary'].fillna(employees['salary'].mean(), inplace=True)
print("🧩 After Filling Missing Salaries with Mean:")
print(employees, "\n")

# -------------------------------
# 6️⃣ Aggregation & GroupBy
# -------------------------------
avg_salary_by_dept = employees.groupby('dept')['salary'].mean().reset_index()
print("📈 Average Salary by Department:")
print(avg_salary_by_dept, "\n")

# -------------------------------
# 7️⃣ Merging / Joining DataFrames
# -------------------------------
merged = pd.merge(employees, departments, on='dept', how='left')
print("🤝 After Joining with Departments:")
print(merged, "\n")

# -------------------------------
# 8️⃣ Removing Duplicates
# -------------------------------
duplicate_df = pd.concat([employees, employees.iloc[0:2]])  # add duplicates
cleaned = duplicate_df.drop_duplicates(subset=['emp_id'])
print("🧹 After Removing Duplicates:")
print(cleaned, "\n")

# -------------------------------
# 9️⃣ String operations
# -------------------------------
employees['name_upper'] = employees['name'].str.upper()
print("🔠 Names Converted to Uppercase:")
print(employees[['name', 'name_upper']], "\n")

# -------------------------------
# 🔟 Apply / Lambda
# -------------------------------
employees['salary_status'] = employees['salary'].apply(lambda x: 'High' if x > 70000 else 'Low')
print("⚙️ Salary Categorization using Lambda:")
print(employees[['name', 'salary', 'salary_status']], "\n")

# -------------------------------
# 1️⃣1️⃣ Pivot Table
# -------------------------------
pivot = employees.pivot_table(values='salary', index='dept', aggfunc=['mean', 'max'])
print("📊 Pivot Table (Mean & Max Salary per Dept):")
print(pivot, "\n")

# -------------------------------
# 1️⃣2️⃣ Export to CSV
# -------------------------------
employees.to_csv('F:/python_tutorial/pandas/final_employees.csv', index=False)
print("✅ Data exported to 'final_employees.csv'")
