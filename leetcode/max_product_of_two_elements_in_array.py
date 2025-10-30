number=[ -3, 4, 5, -1,8 ]

number.sort()

max_product = max(number[0] * number[1], number[-1] * number[-2])
print(max_product)