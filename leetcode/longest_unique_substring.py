string = "abcdabcdebb"

start = 0
max_length = 0
max_substring = ""
seen = {}

for end, char in enumerate(string):
    if char in seen and seen[char] >= start:
        start = seen[char] + 1   # Move start after the previous duplicate
    seen[char] = end             # Update last seen index
    
    # Calculate current window length
    current_length = end - start + 1
    if current_length > max_length:
        max_length = current_length
        max_substring = string[start:end+1]

print("Longest unique substring:", max_substring)
print("Length:", max_length)