nums = [1, 3, 5, 6, 7, 10]

full_range = set(range(min(nums), max(nums) + 1))
missing = list(full_range - set(nums))
print(sorted(missing))