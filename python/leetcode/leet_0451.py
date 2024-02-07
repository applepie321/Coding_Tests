# Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/description/?envType=daily-question&envId=2024-02-07

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        sorted_chars = sorted(counts, key=lambda x: (-counts[x], x))
        sorted_str = ''.join(char * counts[char] for char in sorted_chars)

        return sorted_str
