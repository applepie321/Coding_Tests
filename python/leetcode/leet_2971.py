# Find Polygon With the Largest Perimeter
# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/description/?envType=daily-question&envId=2024-02-15

def largest_perimeter(nums: list[int]) -> int:
    nums = sorted(nums)
    previous_sum = 0
    answer = -1

    for i in nums:
        if i < previous_sum:
            answer = i + previous_sum
        previous_sum += i
    return answer
