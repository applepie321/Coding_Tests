# Majority Element
# https://leetcode.com/problems/majority-element/description/?envType=daily-question&envId=2024-02-12

def majority_element(nums):
    return max(set(nums), key=nums.count)
