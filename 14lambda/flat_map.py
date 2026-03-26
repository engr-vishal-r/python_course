data = ["hello world", "how are you"]

# flatMap -> split each line into words
result = [word for line in data for word in line.split()]

print(list(result))
# Output: ['hello', 'world', 'how', 'are', 'you']
