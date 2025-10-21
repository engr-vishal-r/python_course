a=100
b=200

MASK = 0xFFFFFFFF
MAX_INT = 0x7FFFFFFF

while b != 0:
    borrow = (~a) & b & MASK
    a = a ^ b & MASK
    b = borrow << 1 & MASK

# Handle overflow for signed integer
if a <= MAX_INT:
    print(a)
else:
    print(~(a ^ MASK))