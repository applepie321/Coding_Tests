# Sum of Subarray Minimums
# https://leetcode.com/problems/sum-of-subarray-minimums/description/?envType=daily-question&envId=2024-01-20

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 10 ** 9 + 7
        dp = [0] * n
        stack = []
        answer = 0

        for i in range(n):
            while len(stack) > 0 and arr[i] <= arr[stack[-1]]:
                stack.pop()
            if len(stack) > 0:
                j = stack[-1]
                dp[i] = dp[j] + arr[i] * (i - j)
            else:
                dp[i] = arr[i] * (i + 1)

            stack.append(i)
            answer = (answer + dp[i]) % mod
        return answer
