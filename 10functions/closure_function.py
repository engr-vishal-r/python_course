# Closure function remembers the variables from its enclosing scope.

def outer(msg):
    def inner():
        print(msg)
    return inner
greet = outer("Hi")
greet()