nums = [1,4,6,7,8,50, 3,"vishal"]
even = list(filter(lambda x: isinstance(x, int) and x % 2 == 0, nums)) if nums else "Enter valid number"
print(even)