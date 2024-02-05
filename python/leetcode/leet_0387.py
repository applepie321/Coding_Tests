# First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=daily-question&envId=2024-02-05

def first_unique_char(s: str) -> int:
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i

    return -1
