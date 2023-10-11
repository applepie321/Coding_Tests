# Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-interview-150




from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multiply_all = reduce(lambda x, y: x*y, nums)
        answer = []
        if nums.count(0) == 1:
            pos_zero = nums.index(0)
            without_zero = nums.remove(0)
            multiply_zero1 = reduce(lambda x, y: x*y, without_zero)
        return multiply_zero1

        elif nums.count(0) > 1:
            for num in ramge(len(nums)):
                answer[num] = 0
            return answer

        else:
            for 
        