def find_duplicate(strings):
    duplicate_strings = []
    seen = []
    for word in strings:
        if word in seen:
            if word not in duplicate_strings:
                duplicate_strings.append(word)
        else:
            seen.append(word)
    if len(duplicate_strings) ==0:
        return "No duplicates found"
    return duplicate_strings

if __name__ == "__main__":
    strings = ["vishal", "ramesh", "vijay", "vishal", "latha"]
    print(find_duplicate(strings))