def largest(nums):
    sorted_num=sorted(set(nums), reverse=True)
    return sorted_num[2]

nums = [15, 5, 9, 20, 3, 3]
print(largest(nums))