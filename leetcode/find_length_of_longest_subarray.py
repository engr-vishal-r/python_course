def longest_subarray_sum_k(nums, k):
    prefix_sum = 0
    max_length = 0
    sum_map = {}  # Stores prefix_sum: index

    for i, num in enumerate(nums):
        prefix_sum += num

        # Case 1: Whole subarray from 0 to i has sum = k
        if prefix_sum == k:
            max_length = i + 1

        # Case 2: There exists a subarray ending at i with sum = k
        if (prefix_sum - k) in sum_map:
            max_length = max(max_length, i - sum_map[prefix_sum - k])

        # Store prefix_sum if it's not already present
        if prefix_sum not in sum_map:
            sum_map[prefix_sum] = i

    return max_length

# Test
nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8
print("Length of longest subarray with sum =", k, "is:", longest_subarray_sum_k(nums, k))