# Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/description/?envType=daily-question&envId=2024-03-02

def sorted_squares(nums):
    answer = []
    for i in nums:
        answer.append(i * i)

    return sorted(answer)
