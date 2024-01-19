# Minimum Falling Path Sum
# https://leetcode.com/problems/minimum-falling-path-sum/?envType=daily-question&envId=2024-01-19

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        if m == 1 or n == 1:
            return matrix[0][0]

        dp = [[0] * m for _ in range(n)]

        for j in range(m):
            dp[0][j] = matrix[0][j]

        # up = directly above
        # ld = diagonally up-left
        # rd = diagonally up-right
        for i in range(1, n):
            for j in range(m):
                ld = rd = float('inf')
                up = matrix[i][j] + dp[i - 1][j]

                if j - 1 >= 0:
                    ld = matrix[i][j] + dp[i - 1][j - 1]
                if j + 1 < m:
                    rd = matrix[i][j] + dp[i - 1][j + 1]

                dp[i][j] = min(up, min(ld, rd))

        mini = dp[n - 1][0]
        for j in range(1, m):
            mini = min(mini, dp[n - 1][j])
        return mini
