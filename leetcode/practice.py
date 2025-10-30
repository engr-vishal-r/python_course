string="abcdabcabcde"

start=0
seen={}
max_length=0
max_substring=""

for end, char in enumerate(string):
    if char in seen and seen[char] >= start:
        start=seen[char]+1
    seen[char]=end
    current_length=end - start +1
    if current_length > max_length:
        max_length=current_length
        max_substring=string[start:end+1]


print(max_length)
print(max_substring)