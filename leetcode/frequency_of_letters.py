from collections import Counter

text = "India is My Country"
# Remove spaces and convert to lowercase
filtered_text = text.replace(" ", "").lower()

# Count frequency using Counter
letter_freq = Counter(filtered_text)

# Print the result
for letter, freq in letter_freq.items():
    print(f"{letter}: {freq}")