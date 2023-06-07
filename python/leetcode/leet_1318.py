# 1318. Minimum Flips to Make a OR b Equal to c
# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/description/


# Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.


# Example 1:
# Input: a = 2, b = 6, c = 5
# Output: 3
# Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)



# Example 2:
# Input: a = 4, b = 2, c = 7
# Output: 1


# Example 3:
# Input: a = 1, b = 2, c = 3
# Output: 0


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        for i in range(31):
            # i'th bit of c is 1
            if (c >> i) & 1:
                flips += ((a >> i) & 1) == 0 and ((b >> i) & 1) == 0
            # i'th bit of c is 0
            else:
                flips += (a >> i) & 1
                flips += (b >> i) & 1
        return flips
    

# Soultion Source: https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/solutions/3606850/clear-and-intuitive-explanation-of-bit-manipulation-python/