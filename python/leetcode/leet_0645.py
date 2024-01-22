# Set Mismatch
# https://leetcode.com/problems/set-mismatch/description/?envType=daily-question&envId=2024-01-22

from typing import List


def findErrorNums(self, nums: List[int]) -> List[int]:
    n = len(nums)
    original_sum = n * (n + 1) // 2
    actual_sum = sum(set(nums))
    duplicate = sum(nums) - actual_sum
    missing = original_sum - actual_sum

    return [duplicate, missing]
