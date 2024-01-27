# K Inverse Pairs Array
# https://leetcode.com/problems/k-inverse-pairs-array/description/?envType=daily-question&envId=2024-01-27

def k_inverse_pairs(n, k) -> int:
    # Keep numbers within integer bounds
    mod = 10**9 + 7

    # count of inverse pairs
    dp = [1] + [0] * k
    # inner loop
    prefix_sum = [0] * (k + 2)

    for current_number in range(1, n + 1):
        for inverse_count in range(1, k + 1):
            dp[inverse_count] = (prefix_sum[inverse_count + 1] -
                                 prefix_sum[max(0, inverse_count - (current_number))]) % mod

        for index in range(1, k + 2):
            prefix_sum[index] = (prefix_sum[index - 1] + dp[index - 1]) % mod

    return dp[k]
