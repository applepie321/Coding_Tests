# Missing Number
# https://leetcode.com/problems/missing-number/description/?envType=daily-question&envId=2024-02-20

def missing_number(nums: list[int]) -> int:
    original_nums = set(range(len(nums) + 1))
    missing_num = original_nums - set(nums)
    return missing_num.pop()
