num = [3, 3, 5, 4, 3, 4, 4, 4, 4]
counts = {}
majority_element = None

for n in num:
    counts[n] = counts.get(n, 0) + 1
    if counts[n] > len(num) // 2:
        majority_element = n
        break

print("Majority Element:", majority_element)