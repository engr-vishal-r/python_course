chars = ['a', 'c', 'b', 'd']
lst = sorted(chars)

print("Substrings:")

n = len(lst)

for length in range(1, n + 1):  # window size
    for i in range(n - length + 1):  # start index of window
        substring = lst[i:i + length]
        print(' '.join(substring))