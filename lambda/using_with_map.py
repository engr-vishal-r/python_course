nums = [5, 3, 8]

squares = list(map(lambda x: x**2, filter(lambda x: isinstance(x, int), nums))) if nums else "arguments required"

print(squares)
