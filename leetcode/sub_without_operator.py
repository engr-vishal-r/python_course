import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customException.numberexceptionerror import NumberFormatExceptionError

def subtract(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise NumberFormatExceptionError("Both a and b must be integers")
    
    MASK = 0xFFFFFFFF
    MAX_INT = 0x7FFFFFFF
    
    while b != 0:
        borrow = ((~a) & b) & MASK
        a = (a ^ b) & MASK
        b = (borrow << 1) & MASK
    
    if a <= MAX_INT:
        return a
    else:
        return (~(a ^ MASK))

    
# Test with invalid input
print(subtract(10, 500))