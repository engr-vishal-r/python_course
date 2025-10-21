string="COOMPUUTEEER"
vowels="AEIOU"
cleaned_string=""
prev_char=""

for char in string:
    if char in vowels and prev_char in vowels:
        continue
    cleaned_string += char
    prev_char = char

print("Cleaned String : ", cleaned_string)