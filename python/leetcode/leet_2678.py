# Number of Senior Citizens
# https://leetcode.com/problems/number-of-senior-citizens/description/?envType=daily-question&envId=2024-08-01
from typing import List


def count_seniors(details: List[str]) -> int:
    return sum(int(detail[-4:-2]) > 60 for detail in details)
