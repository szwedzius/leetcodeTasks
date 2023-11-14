def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    letters = [0] * 26
    for i in range(0, len(s)):
        letters[ord(s[i]) - 97] += 1
        letters[ord(t[i]) - 97] -= 1

    return letters == [0] * 26


print(is_anagram("anagram", "nagaram"))
print(is_anagram("cat", "rat"))
print(is_anagram("bitch", "tibch"))
