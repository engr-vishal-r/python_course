strings = ["he", "yellow", "helo", "hello","hello"]
target = "hell"

for word in strings:
    if target in word:
        print(f"Contains '{target}': {word}")
