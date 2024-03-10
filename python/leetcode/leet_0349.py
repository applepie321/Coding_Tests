# Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/?envType=daily-question&envId=2024-03-10

def intersection(nums1, nums2):
    answer = [item for item in nums1 if item in nums2]
    return set(answer)
