input=[1,2,3,4,5,6]

target=11

for i in range(len(input)):
    for j in range(i+1, len(input)):
        if input[i]+input[j] == target:
            print(input[i], input[j])