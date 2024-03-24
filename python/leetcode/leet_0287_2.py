# Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/?envType=daily-question&envId=2024-03-24

from collections import Counter


def find_duplicate(nums: list[int]) -> int:
    nums_count = Counter(nums)
    answer = nums_count.most_common(1)
    return answer[0][0]
