# Perfect Squares
# https://leetcode.com/problems/perfect-squares/description/?envType=daily-question&envId=2024-02-08

def num_squares(n):
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = i

        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1

    return dp[n]
