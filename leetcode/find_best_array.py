nums = [1, 3, -4, 1, -2, 1, 5, 4]
k = 4

# Initialize the first window
window_sum = sum(nums[:k])
max_sum = window_sum
best_start = 0

# Slide the window
for i in range(k, len(nums)):
    window_sum += nums[i] - nums[i - k]
    if window_sum > max_sum:
        max_sum = window_sum
        best_start = i - k + 1

best_subarray = nums[best_start:best_start + k]
print(f"Best subarray of length {k}: {best_subarray}, Max Sum: {max_sum}")
