chars = ['a', 'c', 'b', 'd']
lst = sorted(chars)

print("Substrings:")

n = len(lst)
for i in range(n):
    substring = []  # start new substring
    for j in range(i, n):
        substring.append(lst[j])  # add next char
        print(' '.join(substring))  # print current substring