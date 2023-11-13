# Sort Vowels in a String
# https://leetcode.com/problems/sort-vowels-in-a-string/description/?envType=daily-question&envId=2023-11-13


class Solution:
    def sortVowels(self, s: str) -> str:
        
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        vowels_index = [i for i, char in enumerate(s) if char in vowels]
        vowels_sorted = sorted([s[i] for i in vowels_index])

        result = list(s)
        for i, index in enumerate(vowels_index):
            result[index] = vowels_sorted[i]
        return ''.join(result)
