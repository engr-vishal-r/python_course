from itertools import combinations

input=['a','b','d','c']

for i in range(len(input)):
    for j in range(0, len(input) -i -1):
        if input[j] > input[j+1]:
            temp=input[j]
            input[j]=input[j+1]
            input[j+1]=temp

for length in range(1,len(input)+1):
    for combo in combinations(input, length):
        print(''.join(combo))
