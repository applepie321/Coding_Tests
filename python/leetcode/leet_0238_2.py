# Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/?envType=daily-question&envId=2024-03-15

def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    left = [1] * n
    right = [1] * n
    answer = [1] * n

    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    for i in range(n):
        answer[i] = left[i] * right[i]

    return answer
