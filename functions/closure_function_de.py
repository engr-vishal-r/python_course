def add_field(field_name, default_value):
    def transformer(record):
        record[field_name] = default_value
        return record
    return transformer

transform = add_field("processed", True)
print(transform({"id": 1})) 
