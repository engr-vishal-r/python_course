class DataTransformer:
    schema = {"id": int, "name": str, "salary": float}

    def __init__(self, record):
        self.record = record

    @staticmethod
    def clean_string(value):
        return value.strip().title()

    @classmethod
    def validate_schema(cls, record):
        return all(key in record for key in cls.schema)


print(DataTransformer.clean_string("   vishal  "))
record = {"id": 1, "name": "Alice", "salary": 5000}
print(DataTransformer.validate_schema(record))
