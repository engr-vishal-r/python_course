class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor  is implicitly called in this case. If you need to customize the constructor, you can explicitly use it.
        self.breed = breed

    def speak(self):
        print(f"{self.name} the {self.breed} says Woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")


dog1 = Dog("Dog", "husky")
cat1 = Cat("Cat")

# Call methods
dog1.speak()   
cat1.speak()  