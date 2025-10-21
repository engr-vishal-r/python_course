def check_anagrams(string_1, string_2):
    if sorted(string_1) == sorted(string_2):
        return (f"Strings are Anagram")
    else:
        return (f"Strings are not Anagram")
    
if __name__ == "__main__":
    print(check_anagrams("vijay", "jayvi"))
    