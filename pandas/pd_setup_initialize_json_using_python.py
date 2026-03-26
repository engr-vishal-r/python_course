import pandas as pd

json_df=pd.read_json("file:///F:/python_tutorial/pyspark/employees.json") 

#Selecting Data
# Columns
print(json_df['salary'])
print(json_df[['name', 'dept_id']])

# Rows
print(json_df.iloc[0])            # Row by position
print(json_df.loc[2])             # Row by index label

# Filtering
# json_df[json_df['salary'] > 50000]
print(json_df[(json_df['dept_id'] == 3) & (json_df['salary'] > 70000)])

print(json_df.isnull().sum())                   # Count missing values
print(json_df.fillna(0, inplace=True))          # Replace missing with 0
print(json_df.dropna(inplace=True))             # Drop rows with missing
json_df['name'] = json_df['name'].str.strip()   # Strip spaces
print(json_df['name'])

# Step 1: Convert joining_date to datetime
json_df['joining_date'] = pd.to_datetime(json_df['joining_date'], errors='coerce')

# Step 2: Group by name and get max/min hire dates
agg_df = json_df.groupby('name').agg(
    latest_hire=('joining_date', 'max'),
    first_hire=('joining_date', 'min')
).reset_index()
"""
agg_df = json_df.groupby('name').agg(
     hire_span_days=('joining_date', lambda x: (x.max() - x.min()).days)
).reset_index()
"""
# Step 3: Calculate days between hires
agg_df['days_between_hires'] = (agg_df['latest_hire'] - agg_df['first_hire']).dt.days

# Step 4: View result
print(agg_df)

agg_df.to_csv("F:/python_tutorial/pandas/hire_summary.csv", index=False)
print("Output written in CSV File")