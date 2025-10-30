input=[1,2,3,4,5,6]

target=5

for i in range(len(input)+1):
    for j in range(i, len(input)):
        if input[i]+input[j] == target:
            print(input[i], input[j])