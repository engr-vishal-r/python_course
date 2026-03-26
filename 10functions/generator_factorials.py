def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        yield fact

# Print all factorials up to 8!
for f in factorial(8):
    print(f)