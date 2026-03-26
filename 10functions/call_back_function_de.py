#Use case: Run a function after a stage is completed, e.g., after extraction, trigger transformation.

def extract(callback):
    data = ["raw1", "raw2"]
    print("Extracted data")
    callback(data)

def transform(data):
    print("Transformed data:", [d.upper() for d in data])

# Pass `transform` as a callback to `extract`
extract(transform)
