#Partially Applied Function
#Using functools.partial to fix some arguments of a function.
#A partially applied function is a technique where you "pre-fill" some arguments of a function, creating a new function with fewer arguments.

from functools import partial

def power(base, exponent):
    return base ** exponent
square = partial(power, exponent=2)

print(power(3,2))

print(square(3))