# Divide Array Into Arrays With Max Difference
# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/?envType=daily-question&envId=2024-02-01

def divide_array(nums, k):
    nums.sort()
    answer = []
    for i in range(0, len(nums), 3):
        if nums[i + 2] - nums[i] > k:
            return []
        answer.append([nums[i], nums[i + 1], nums[i + 2]])
    return answer
