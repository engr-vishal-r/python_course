def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

print(add(70, 5))