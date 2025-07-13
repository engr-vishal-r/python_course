trips={
    "dv001":{
    "driver_id": "dv001",
    "model":"suzuki",
    "make":2022,
    "color":"white",
    "driver":"Vishal",
    "car_number":"TN01A0001",
    "fare": 550.50,
    "drop_location": "tnagar",
    "completed": True
},
 "dv002":{
    "driver_id": "dv002",
    "model":"suzuki",
    "make":2020,
    "color":"white",
    "driver":"Rajesh",
    "car_number":"TN05A0005",
    "fare": 1050.50,
    "drop_location": "Tambaram",
    "completed": True
},
 "dv003":{
    "driver_id": "dv003",
    "model":"tata",
    "make":2024,
    "color":"white",
    "driver":"Sathish",
    "car_number":"TN23A0023",
    "fare": 850.50,
    "drop_location": "vellore",
    "completed": True
}
}

for trip in trips.items():
    print(trip)

print()
      
for trip_id, trip_details in trips.items():
    print(f"{trip_id} -> driver_id: {trip_details['driver_id']}")