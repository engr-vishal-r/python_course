string = "LoveCountry"
insert_string = "My"
K = 4

# Insert the string at the Kth position
result = string[:K] + " " + insert_string + " " + string[K:]

print(result)