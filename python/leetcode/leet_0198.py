# House Robber
# https://leetcode.com/problems/house-robber/description/?envType=daily-question&envId=2024-01-21

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        memo = [0] * (len(nums) + 1)
        memo[0] = 0
        memo[1] = nums[0]

        for i in range(1, len(nums)):
            val = nums[i]
            memo[i+1] = max(memo[i], memo[i-1] + val)

        return memo[len(nums)]
