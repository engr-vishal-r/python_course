import pandas as pd

# Create Person DataFrame
person = {
    "personId": [1, 2],
    "lastName": ["Wang", "Alice"],
    "firstName": ["Allen", "Bob"]
}
person = pd.DataFrame(person)

# Create Address DataFrame
address = {
    "addressId": [1, 2],
    "personId": [2, 3],
    "city": ["New York City", "Leetcode"],
    "state": ["New York", "California"]
}
address = pd.DataFrame(address)

# LEFT JOIN on personId
result = pd.merge(person, address, on="personId", how="left")

result["city"] = result["city"].fillna("UNKNOWN")
result["state"] = result["state"].fillna("UNKNOWN")

# Select required columns
result = result[["firstName", "lastName", "city", "state"]]

print(result)