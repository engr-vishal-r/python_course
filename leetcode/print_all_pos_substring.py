from itertools import combinations

input=['a','b','d','c']

sorted_list=sorted(input)

n =len(sorted_list)

for length in range(1,n+1):
    for combo in combinations(sorted_list, length):
        print(''.join(combo))
