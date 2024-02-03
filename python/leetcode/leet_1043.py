# Partition Array for Maximum Sum
# https://leetcode.com/problems/partition-array-for-maximum-sum/description/?envType=daily-question&envId=2024-02-03

def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        max_val = 0
        for j in range(1, min(k, i) + 1):
            max_val = max(max_val, arr[i - j])
            dp[i] = max(dp[i], dp[i - j] + max_val * j)
        return dp[n]
