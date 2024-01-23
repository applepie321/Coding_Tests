# Maximum Length of a Concatenated String with Unique Characters
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/?envType=daily-question&envId=2024-01-23

# Bit Operation

def maxLength(self, arr) -> int:
    dp = [0]
    res = 0
    for substring in arr:
        a = 0
        dup = 0
        for char in substring:
            dup |= a & (1 << (ord(char) - ord('a')))
            a |= 1 << (ord(char) - ord('a'))
        if dup > 0:
            continue
        for i in range(len(dp) - 1, -1, -1):
            if (dp[i] & a) > 0:
                continue
            dp.append(dp[i] | a)
            res = max(res, bin(dp[i] | a).count('1'))
    return res

# dp = dynamic programming
# dup: Bitmask  = This variable is used to check for duplicate characters within a substring.
# a: Bitmask = This variable is used to represent the unique characters within a substring.
