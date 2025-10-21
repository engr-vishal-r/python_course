words = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = {}

for word in words:
    sorted_word = ''.join(sorted(word))

    if sorted_word not in anagrams:
        anagrams[sorted_word]=[]
    anagrams[sorted_word].append(word)

grouped_anagrams = list(anagrams.values())
print(grouped_anagrams)