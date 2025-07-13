class Father:
    def skills(self):
        print("Father: Gardening, Driving")

class Mother:
    def skills(self):
        print("Mother: Cooking, Painting")

class Child(Father, Mother):
    def skills(self):
        # Override both parents' method
        print("Child: Programming, Gaming")

# Object
c = Child()
c.skills()