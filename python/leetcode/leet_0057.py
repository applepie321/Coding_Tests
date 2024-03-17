# Insert Interval
# https://leetcode.com/problems/insert-interval/description/?envType=daily-question&envId=2024-03-17

def insert(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    result.append(newInterval)

    return result
