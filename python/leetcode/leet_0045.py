# Jump Game II
# https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150


# You are given a 0-indexed array of integers nums of length n.
# You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump 
# from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. 
# The test cases are generated such that you can reach nums[n - 1].



class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        current_max = 0
        next_max = 0

        for i in range(n):
            next_max = max(next_max, i + nums[i])

            if i == current_max:
                jumps += 1
                current_max = next_max

            if current_max >= n - 1:
                break
        return jumps