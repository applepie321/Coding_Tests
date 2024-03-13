# Find the Pivot Integer
# https://leetcode.com/problems/find-the-pivot-integer/description/?envType=daily-question&envId=2024-03-13

def pivot_integer(n: int) -> int:
    left = 0
    right = sum(range(1, n + 1))

    for x in range(1, n + 1):
        right -= x
        if left == right:
            return x
        left += x

    return -1
