def count_char(string):
    count = sum(char.isupper() for s in string for char in s )
    return count


if __name__ == "__main__":
    print(count_char(["IndiA Is My Country","Love India"]))