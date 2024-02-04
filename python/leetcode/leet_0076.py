# Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/description/?envType=daily-question&envId=2024-02-04

from collections import Counter


def min_window(s, t):
    if not s or not t:
        return ""

    target_count = Counter(t)
    required = len(target_count)
    formed = 0
    window_count = {}
    left, right = 0, 0
    ans = float('inf'), None, None

    while right < len(s):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1
        if char in target_count and window_count[char] == target_count[char]:
            formed += 1
        while formed == required:
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            char = s[left]
            window_count[char] -= 1
            if char in target_count and window_count[char] < target_count[char]:
                formed -= 1
            left += 1
        right += 1
    return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]
