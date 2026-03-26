from collections import Counter

string=["LoveMyCountry", "RaceCar"]

vowels="aeiouAEIOU"

vowel_chars = [ch for word in string for ch in word if ch in vowels]

# Count frequency of vowels
frequency = Counter(vowel_chars)
for key,value in frequency.items():
    print(key,value)