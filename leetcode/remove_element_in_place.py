input=[3,1,5,6,7,9,8]

val=3

k=0

for i in range(len(input)):
    if input[i] != val:
        input[k] = input[i]
        k += 1

print(input[:k])