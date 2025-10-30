words = ["aba", "aabb", "abcd", "bac", "aabc"]

count = 0

for i in range(len(words)):
    for j in range(i + 1, len(words)):
        set_i = set(words[i])
        set_j = set(words[j])
        if set_i == set_j:
            count += 1

print(count)