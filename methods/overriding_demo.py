class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  # This overrides Animal's speak()
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat Says Meoww!!")

d = Dog()
d = Cat()
d.speak()  # Output: Dog barks