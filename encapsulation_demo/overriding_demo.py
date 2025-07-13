class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  # This overrides Animal's speak()
        print("Dog barks")

d = Dog()
d.speak()  # Output: Dog barks