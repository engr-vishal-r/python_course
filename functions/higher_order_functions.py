import pandas as pd
df = pd.DataFrame({'name': ['John', 'Alice'], 'salary': [5000, 7000]})
df['bonus'] = df['salary'].apply(lambda x: x * 0.1)

for index, row in df.iterrows():
    print(row['name'], row['salary'], row['bonus'])