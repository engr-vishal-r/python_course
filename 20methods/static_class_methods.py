class DataTransformer:
    schema = {"id": int, "name": str, "salary": float}

    def __init__(self, record):
        self.id = record["id"]
        self.name = record["name"]
        self.salary = record["salary"]
    
    def emp_details(self):
        return self.id,self.name,self.salary

    @staticmethod
    def clean_string(value):
        return value.strip().title()

    @classmethod
    def validate_schema(cls, record):
        return all(key in record for key in cls.schema)



print(DataTransformer.clean_string("   vishal  "))
record = {"id": 1, "name": "Alice", "salary": 5000}
print(DataTransformer.validate_schema(record))
emp=DataTransformer(record)
print(emp.emp_details())