# Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/?envType=daily-question&envId=2024-03-24

from collections import Counter


def find_duplicate(nums: list[int]) -> int:
    count = Counter(nums)
    return max(count, key=count.get)
