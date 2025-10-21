string = ["hello", "man"]
print("reversed_string using slicing :", ' '.join(word[::-1] for word in string[::-1]))

print("reversed_string using reversed method : ", ' '.join(''.join(reversed(word)) for word in string[::-1]))

reversed=""
for i in range(len(string)-1,-1,-1):
    reversed += string[i][::-1] + " "

print(reversed.strip())