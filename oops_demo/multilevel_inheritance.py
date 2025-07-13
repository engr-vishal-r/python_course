# Base Class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print(f"{self.brand} is moving on the road.")

# First Level Derived Class
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def fuel_type(self):
        print(f"{self.brand} {self.model} uses petrol or diesel.")

# Second Level Derived Class
class ElectricCar(Car):
    def __init__(self, brand, model, battery_range):
        super().__init__(brand, model)
        self.battery_range = battery_range

    def fuel_type(self):
        print(f"{self.brand} {self.model} is an electric car with {self.battery_range} km range.")

# Create object
tesla = ElectricCar("Tesla", "Model 3", 500)
tesla.move()         # Inherited from Vehicle
tesla.fuel_type()    # Overridden method in ElectricCar