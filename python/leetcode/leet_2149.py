# Rearrange Array Elements by Sign
# https://leetcode.com/problems/rearrange-array-elements-by-sign/?envType=daily-question&envId=2024-02-14

def rearrange_array(nums: list[int]) -> list[int]:
    answer = [0] * len(nums)

    pos_pointer = 0
    neg_pointer = 1

    for i in range(len(nums)):
        if nums[i] > 0:
            answer[pos_pointer] = nums[i]
            pos_pointer += 2
        else:
            answer[neg_pointer] = nums[i]
            neg_pointer += 2

    return answer
