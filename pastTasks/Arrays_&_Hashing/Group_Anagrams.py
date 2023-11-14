def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    anagram_dictionary = {}
    for string in strs:
        current_word = [0] * 26
        for char in string:
            current_word[ord(char)-ord('a')] += 1

        anagram_id = ""
        for i in range(0, len(current_word)):
            if current_word[i] != 0:
                anagram_id += chr(i + ord('a')) + str(current_word[i])

        if anagram_dictionary.get(anagram_id) is not None:
            anagram_dictionary[anagram_id].append(string)
        else:
            anagram_dictionary[anagram_id] = [string]

    return [*anagram_dictionary.values()]


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))
