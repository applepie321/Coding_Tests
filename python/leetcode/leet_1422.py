# Maximum Score After Splitting a String
# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        zeros_left = 0
        ones_right = s.count('1')

        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros_left += 1
            else:
                ones_right -= 1

            max_score = max(max_score, zeros_left + ones_right)

        return max_score
