# Minimum Number of Operations to Make Array Empty
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/description/?envType=daily-question&envId=2024-01-04

from collections import Counter


class Solution:
    def minOperations(self, nums: list[int]) -> int:

        frequency = Counter(nums)

        count = 0
        for i in frequency.values():
            if i == 1:
                return -1
            count += i // 3

            if i % 3:
                count += 1
        return count
