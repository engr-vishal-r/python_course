order_by_first_alphabets = ["ate", "tea", "man", "eat", "nam", "anm"]

# Bubble sort by first alphabet
for i in range(len(order_by_first_alphabets)):
    for j in range(i + 1, len(order_by_first_alphabets)):
        if order_by_first_alphabets[i][0] > order_by_first_alphabets[j][0]:
            order_by_first_alphabets[i], order_by_first_alphabets[j] = order_by_first_alphabets[j], order_by_first_alphabets[i]

print(order_by_first_alphabets)