# Meeting Rooms III
# https://leetcode.com/problems/meeting-rooms-iii/description/?envType=daily-question&envId=2024-02-18

import math


def most_booked(n: int, meetings: list[list[int]]) -> int:
    # RAT = Room Availability Time
    RAT = [0] * n
    meeting_count = [0] * n

    for start, end in sorted(meetings):
        # Min Room Availability Time
        MRAT = math.inf

        # Min Available Time Room
        MATR = 0

        found_unused_room = False
        for i in range(n):
            if RAT[i] <= start:
                found_unused_room = True
                meeting_count[i] += 1
                RAT[i] = end
                break
            if MRAT > RAT[i]:
                MRAT = RAT[i]
                MATR = i
        if not found_unused_room:
            RAT[MATR] += end - start
            meeting_count[MATR] += 1
    return meeting_count.index(max(meeting_count))
