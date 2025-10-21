string="COOMPUTEER"
vowels="AEIOU"

consecutive_vowel=[]
prev_char=""

for char in string:
    if char in vowels and prev_char in vowels:
        consecutive_vowel.append(prev_char)
    prev_char = char
        
print(consecutive_vowel)