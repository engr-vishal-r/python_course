#Group by Key (List of Dicts to Nested Dict)
from collections import defaultdict

data = [{'dept': 'HR', 'name': 'Alice'}, {'dept': 'IT', 'name': 'Bob'}, {'dept': 'HR', 'name': 'Eve'}]
result = {}

for item in data:
    dept=item['dept']
    name=item['name']

    if dept not in result:
        result[dept]=[]

    result[dept].append(name)

print(result)  