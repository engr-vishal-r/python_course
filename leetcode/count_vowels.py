from collections import Counter

string="LoveMyCountry"

vowels="aeiouAEIOU"

vowel_chars = [ch for ch in string if ch in vowels]

# Count frequency of vowels
frequency = Counter(vowel_chars)
for key,value in frequency.items():
    print(key,value)