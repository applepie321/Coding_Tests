# Furthest Building You Can Reach
# https://leetcode.com/problems/furthest-building-you-can-reach/description/?envType=daily-question&envId=2024-02-17
import heapq


def furthest_building(heights: list[int], bricks: int, ladders: int) -> int:
    memo = []

    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff > 0:
            heapq.heappush(memo, diff)
            if len(memo) > ladders:
                bricks -= heapq.heappop(memo)
            if bricks < 0:
                return i
    return len(heights) - 1
