# 1913. Maximum Product Difference Between Two Pairs
# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/?envType=daily-question&envId=2023-12-19

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        return sorted_nums[-1] * sorted_nums[-2] - sorted_nums[0] * sorted_nums[1]
