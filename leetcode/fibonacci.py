# Python program to generate Fibonacci series using a temporary variable

# Take number of terms from the user
n = int(input("Enter number of terms: "))

# First two terms
a = 0
b = 1

print("Fibonacci series: ")

for _ in range(n):
    print(a, end=" ")
    
    temp = a + b   # Calculate next term
    a = b          # Move b to a
    b = temp       # Move next term to b