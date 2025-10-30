from collections import Counter

def firstUniqChar(s):
    freq = Counter(s)             # Count frequency of each character
    for i, ch in enumerate(s):    # Loop through string with index
        if freq[ch] == 1:         # If character appears only once
            return i              # Return its index
    return -1                     # If no unique character found

s = "loveleetcode"
print(firstUniqChar(s))  # Output: 2  (since 'v' is the first unique)