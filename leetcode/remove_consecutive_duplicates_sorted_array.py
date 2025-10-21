def removeDuplicates(nums):
    if not nums:
        return 0
    
    # Initialize pointer for unique elements
    k = 1  

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k

nums = [1,1,2,3,3]
k = removeDuplicates(nums)
print(nums[:k]) 