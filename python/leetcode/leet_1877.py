# Minimize Maximum Pair Sum in Array
# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/?envType=daily-question&envId=2023-11-17

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()

        left, right = 0, len(nums) -1

        result = 0

        while left < right:
            result = max(result, nums[left] + nums[right])
            left += 1
            right -= 1

        return result