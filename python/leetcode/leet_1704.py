# Determine if String Halves Are Alike
# https://leetcode.com/problems/determine-if-string-halves-are-alike/description/?envType=daily-question&envId=2024-01-12

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        half = int(len(s) / 2)
        head = s[:half]
        tail = s[half:]

        count_head = sum(1 for char in head if char in vowels)
        count_tail = sum(1 for char in tail if char in vowels)

        return count_head == count_tail
