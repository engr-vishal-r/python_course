my_dict = [{
    "name": "Ramesh",
    "age": 30,
    "location": "Bangalore"
},{
    "name": "Dinesh",
    "age": 20,
    "location": "Chennai",
    "name":"Naresh"  #overriden
},{
    "name": "Dinesh",
    "age": 20,
    "location": "Chennai"
}]

for person in my_dict:
    if person["age"] > 25:
        person["status"] = "senior"
    else:
        person["status"] = "junior"
    for k,v in person.items():
        print(f"{k}: {v}")

key_value_pairs=list(map(lambda item: list(item.items()), my_dict))
print(key_value_pairs)  