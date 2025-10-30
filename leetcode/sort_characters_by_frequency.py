from collections import Counter


def frequencySort(s):
    freq=Counter(s)

     # Sort characters by frequency (descending), then by character (optional)
    sorted_chars = sorted(freq.items(), key=lambda x: -x[1])
    
    # Build result string by repeating each character by its frequency
    result = ''.join(char * count for char, count in sorted_chars)
    return result

s = "tree"
print(frequencySort(s))  # Output: "eetr" or "eert"