words="COMPUTER"
vowels="AEIOU"
count=0

for char in words:
    if char in vowels:
        count += 1

print("Count of Vowels  :", count)