input = ['a', 'e', 'd', 'b']

for i in range(len(input)):
    for j in range(0, len(input) - i - 1):
        if input[j] > input[j + 1]:
            # swap
            temp = input[j]
            input[j] = input[j + 1]
            input[j + 1] = temp

print("Sorted list:", input)
