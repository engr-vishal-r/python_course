#Higher-Order Function (HOF) that takes another function as argument or returns one.
def apply(func, value):
    return func(value)
print(apply(lambda x: x*2, 5))  