# 1502. Can Make Arithmetic Progression From Sequence

# A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

# Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.


# Input: arr = [3,5,1]
# Output: true
# Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.


# Input: arr = [1,2,4]
# Output: false
# Explanation: There is no way to reorder the elements to obtain an arithmetic progression.






class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sortArr = sorted(arr)
        for i in range(len(arr)-2):
            if sortArr[i+1] - sortArr[i] != sortArr[i+2] - sortArr[i+1]:
                return False
        return True