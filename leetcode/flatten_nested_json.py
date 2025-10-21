def flatten_json(d, parent_key='', sep='_'):
    items = {}

    if isinstance(d, dict):
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.update(flatten_json(v, new_key, sep))
            elif isinstance(v, list):
                for i, item in enumerate(v):
                    items.update(flatten_json(item, f"{new_key}{sep}{i}", sep))
            else:
                items[new_key] = v
    else:
        items[parent_key] = d

    return items

nested = {"app":"2025429238INR","users": [{"individualUser": {"name": "Alice", "address": {"city": "NY","pin":632508}}},{"ManagerUser": {"name": "English", "address": {"city": "NY","pin":600001}}}]}
print(flatten_json(nested))