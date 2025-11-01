import pandas as pd

# Create Person DataFrame
person_data = {
    "personId": [1, 2],
    "lastName": ["Wang", "Alice"],
    "firstName": ["Allen", "Bob"]
}
person = pd.DataFrame(person_data)

# Create Address DataFrame
address_data = {
    "addressId": [1, 2],
    "personId": [2, 3],
    "city": ["New York City", "Leetcode"],
    "state": ["New York", "California"]
}
address = pd.DataFrame(address_data)

# LEFT JOIN on personId
result = pd.merge(person, address, on="personId", how="left")

# Select required columns
result = result[["firstName", "lastName", "city", "state"]]

print(result)
