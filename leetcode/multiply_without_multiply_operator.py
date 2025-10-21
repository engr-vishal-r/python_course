def multiply(a, b):
    result = 0
    negative = False

    # Handle negative numbers
    if a < 0:
        a = -a
        negative = not negative
    if b < 0:
        b = -b
        negative = not negative

    for _ in range(b):
        result += a

    return -result if negative else result

# Example
print(multiply(4, 3))
print(multiply(-4, 3))