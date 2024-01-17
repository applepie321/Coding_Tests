# Unique Number of Occurrences
# https://leetcode.com/problems/unique-number-of-occurrences/?envType=daily-question&envId=2024-01-17
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurs = Counter(arr)

        return len(occurs.values()) == len(set(occurs.values()))
