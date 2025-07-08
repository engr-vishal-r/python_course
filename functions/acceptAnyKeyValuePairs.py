def dynamicKeyValue(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

dynamicKeyValue(name="Vishal", age=30, gender="male")