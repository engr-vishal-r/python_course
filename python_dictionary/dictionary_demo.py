trip={
    "model":"suzuki",
    "make":2022,
    "color":"white",
    "driver":"Vishal",
    "car_number":"TN01A0001",
    "fare": 550.50,
    "drop_location": ["tnagar","tambaram","chengalpet","tindivanam"],
    "completed": True
}

print("Print entire trip details  ---> ", trip)

print("Print car model details using get method  ---> ", trip.get("model"))
print("Print car model details using key ---> ", trip["model"])

print(trip.keys())

for key,value in trip.items():
    print(key,":", value)

for location in trip["drop_location"]:
    print(location) 