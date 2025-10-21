number = [1, 3, 5, 6, 7, 10]

missing = [x for x in range(min(number), max(number) + 1) if x not in number]
print("Missing Element : " , missing) 