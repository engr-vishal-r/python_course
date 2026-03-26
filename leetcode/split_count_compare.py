def comparing_word(input):
    word1, word2=input.split("@")

    if len(word1) != len(word2):
        return False
    elif sorted(word1) != sorted(word2):
        return False
        
    return True


input="ather@their"
result=comparing_word(input)
print(result)