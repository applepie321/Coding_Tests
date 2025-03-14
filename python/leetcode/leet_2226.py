class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        left, right = 1, max(candies)

        while left < right:
            mid = (left + right + 1) // 2
            total_children = 0

            for pile in candies:
                total_children += pile // mid

            if total_children >= k:
                left = mid

            else:
                right = mid - 1

        return left
