# 35. Search Insert Position

# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

# Array, Binary Search



# me
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            cnt = 0
            for i in nums:
                if i > target:
                    return cnt
                cnt = cnt + 1
            return len(nums)
        else:
            return nums.index(target)
        




# from users
#    def searchInsert(self, nums, target):
#         i = 0
#         j = len(nums) - 1
#         while(i <= j):
#             pivot = (i + j) // 2
#             if (nums[pivot] == target):
#                 return pivot
#             elif (nums[pivot] > target):
#                 j = pivot - 1
#             else:
#                 i = pivot + 1
#         return i

# Code description:
# Almost the same approach as pure binary search problem.
# Return i (which is the 'left' indicator) because we say that i = pivot + 1 in the case where nums[pivot] < target. 
# So that i indicates the next position after the element smaller than the target, which is what we want for the output.






# import bisect
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         return bisect.bisect_left(nums, target)