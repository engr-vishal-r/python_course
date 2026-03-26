#Function Composition Combining two functions into one.

def add(x): 
    return x + 2
def multiply(x): 
    return x * 3

def compose(f, g):
    return lambda x: f(g(x))

# Compose add and multiply
new_func = compose(add, multiply)

# Now call the composed function with a value
print(new_func(2))  


'''
def filter_valid_rows(df):
    return df.filter("age IS NOT NULL")

def add_country_column(df):
    return df.withColumn("country", lit("India"))

def compose(f, g):
    return lambda x: f(g(x))

pipeline = compose(add_country_column, filter_valid_rows)
final_df = pipeline(raw_df)

'''


'''
def extract_from_csv(file_path):
    return pd.read_csv(file_path)

def transform_data(df):
    return df.dropna().rename(columns=str.lower)

def load_to_db(df):
    df.to_sql("students", con=engine, if_exists="replace")

etl = compose(load_to_db, compose(transform_data, extract_from_csv))

etl("students.csv")

'''