words = {"madam", "racecar", "apple", "noon", "java", "level", "code"}

palindromes = {word for word in words if word == word[::-1]}
non_palindromes = words - palindromes

print("Palindromes:", palindromes)
print("Non-Palindromes:", non_palindromes)