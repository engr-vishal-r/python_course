number = [-3, 4, 5, -1, 6]
number.sort()

# Compute both product options
product1 = number[0] * number[1]    
product2 = number[-1] * number[-2]

# Compare and print the pair with max product
if product1 > product2:
    print(f"Max product pair: ({number[0]}, {number[1]})")
else:
    print(f"Max product pair: ({number[-2]}, {number[-1]})")