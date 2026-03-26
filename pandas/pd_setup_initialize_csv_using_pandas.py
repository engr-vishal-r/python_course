import pandas as pd

df=pd.read_csv("file:///F:/E2E_Projects/uber-etl-pipeline-de-project/data/uber_data.csv",skip_blank_lines=True,
    encoding='utf-8')

print(df.head())         # First 5 rows
print(df.tail(3))        # Last 3 rows
print("--DataFrame Shape --", df.shape)          # (rows, columns)
print("--DataFrame Info --", df.info())         # Schema & memory info
print("--DataFrame Decribe --", df.describe())     # Summary statistics