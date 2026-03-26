class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark

    def display(self):
        print(f"{self.name} passed with {self.mark}%")

s1=Student("vishal",88)
s2=Student("ramesh",93)
s3=Student("vikash",51)

s1.display()
s2.display()
s3.display()