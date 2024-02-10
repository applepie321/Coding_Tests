# Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/description/?envType=daily-question&envId=2024-02-10

def count_substrings(s):
    n = len(s)
    count = 0

    def expand(left, right):
        count_helper = 0
        while left >= 0 and right < n and s[left] == s[right]:
            count_helper += 1
            left -= 1
            right += 1
        return count_helper

    for i in range(n):
        count += expand(i, i)
        count += expand(i, i + 1)

    return count
