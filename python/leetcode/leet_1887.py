# Reduction Operations to Make the Array Elements Equal
# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/?envType=daily-question&envId=2023-11-19

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        result = value = 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]: value += 1
            result += value
        return result
    