#Overloading is not supported in Python. Use *args, **kwargs, defaults to allow any arguments
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(1, 2))        # Output: 3
print(calc.add(1, 2, 3))     # Output: 6
