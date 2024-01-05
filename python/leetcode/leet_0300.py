# Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/submissions/?envType=daily-question&envId=2024-01-05

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
