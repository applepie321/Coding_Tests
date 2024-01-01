# Assign Cookies
# https://leetcode.com/problems/assign-cookies/description/?envType=daily-question&envId=2024-01-01

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        greed_factors = sorted(g)
        cookie_sizes = sorted(s)

        content_children = 0
        i, j = 0, 0

        while i < len(greed_factors) and j < len(cookie_sizes):
            if greed_factors[i] <= cookie_sizes[j]:
                # Assign the cookie to the child
                content_children += 1
                i += 1
            j += 1

        return content_children
