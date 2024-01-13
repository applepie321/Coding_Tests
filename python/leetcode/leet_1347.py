# Minimum Number of Steps to Make Two Strings Anagram
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/?envType=daily-question&envId=2024-01-13

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = [0] * 26
        t_count = [0] * 26

        for char in s:
            s_count[ord(char) - ord('a')] += 1

        for char in t:
            t_count[ord(char) - ord('a')] += 1

        diff = 0
        for i in range(26):
            diff += abs(s_count[i] - t_count[i])

        min_steps = diff // 2

        return min_steps
