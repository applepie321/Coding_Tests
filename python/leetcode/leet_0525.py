# Contiguous Array
# https://leetcode.com/problems/contiguous-array/description/?envType=daily-question&envId=2024-03-16

def find_max_length(nums: list[int]) -> int:
    count = 0
    max_length = 0
    count_dict = {0: -1}

    for i in range(len(nums)):
        count += 1 if nums[i] == 1 else -1

        if count in count_dict:
            max_length = max(max_length, i - count_dict[count])
        else:
            count_dict[count] = i

    return max_length
