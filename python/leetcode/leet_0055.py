# Jump game
# https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150



# You are given an integer array nums. You are initially positioned at the array's first index, 
# and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.





class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if max_reach < i:
                return False
            
            max_reach = max(max_reach, i + nums[i])
            
            
            if max_reach >= len(nums) - 1:
                return True
        
        return False