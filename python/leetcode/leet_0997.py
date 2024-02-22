# Find the Town Judge
# https://leetcode.com/problems/find-the-town-judge/description/?envType=daily-question&envId=2024-02-22
from collections import defaultdict


def find_judge(n: int, trust: list[list[int]]) -> int:
    trust_count = defaultdict(int)
    trusted_by = defaultdict(int)

    for a, b in trust:
        trust_count[b] += 1
        trusted_by[a] += 1

    for i in range(1, n + 1):
        if trust_count[i] == n - 1 and trusted_by[i] == 0:
            return i

    return -1
