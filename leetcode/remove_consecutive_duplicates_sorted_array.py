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

nums = [1,1,3,4,2,4,2,3,3]

#sorting
for i in range(len(nums)):
    for j in range(1, len(nums) -i -1):
        if nums[j] > nums[j+1]:
            temp=nums[j]
            nums[j]=nums[j+1]
            nums[j+1]=temp

k = removeDuplicates(nums)
print(nums[:k]) 