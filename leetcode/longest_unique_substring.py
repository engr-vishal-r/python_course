def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_len = 0
    start_idx = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        if right - left + 1 > max_len:
            max_len = right - left + 1
            start_idx = left
    
    return max_len, s[start_idx:start_idx+max_len]

s = "abcdabcbb"
length, substring = longest_unique_substring(s)
print("Length:", length)
print("Substring:", substring)