# Bitwise AND of Numbers Range
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/?envType=daily-question&envId=2024-02-21

def range_bitwise_and(left: int, right: int) -> int:
    shift = 0

    while left < right:
        left >>= 1
        right >>= 1
        shift += 1

    return left << shift
