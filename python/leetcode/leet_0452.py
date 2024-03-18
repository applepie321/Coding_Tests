# Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/?envType=daily-question&envId=2024-03-18

def find_min_arrow_shots(points: list[list[int]]) -> int:
    if not points:
        return 0

    points.sort(key=lambda x: x[1])

    arrows = 1
    end = points[0][1]

    for start, end_new in points:
        if end < start:
            arrows += 1
            end = end_new

    return arrows
