import pandas as pd
import openpyxl

df=pd.read_json("file:///F:/python_tutorial/pyspark/employees.json")

# Add column
df['tax'] = df['salary'] * 0.1

# Rename columns
df.rename(columns={'emp_id': 'employee_id'}, inplace=True)

# Change data types
df['joining_date'] = pd.to_datetime(df['joining_date'])

dept_mapping = {
    1: 'ENGLISH',
    2: 'TAMIL',
    3: 'HINDI',
    4: 'FRENCH',
    5: 'SPANISH'
}

df['department'] = df['dept_id'].map(dept_mapping)

# Map or replace
#df['dept'] = df['dept_id'].replace({1: 'ENGLISH'})

#drop records with null dept_id
df = df.dropna(subset=['dept_id'])

# Apply a function to a column
df['net_salary'] = df.apply(lambda row: row['salary'] - row['tax'], axis=1)

print(df[['name','department','salary','tax','net_salary']])
# Employees with salary > 70000, show only name and salary
print(df[df['salary'] > 70000][['name', 'salary']])
df.to_excel("F:/python_tutorial/pandas/employee_salary.xlsx",index=False)