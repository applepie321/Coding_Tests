# Crawler Log Folder
# https://leetcode.com/problems/crawler-log-folder/description/?envType=daily-question&envId=2024-07-10

import re
from typing import List

def min_operations(logs: List[str]) -> int:
    depth = 0

    parent = re.compile(r"^\.\./$")
    stay = re.compile(r"^\./$")
    child = re.compile(r"^[a-zA-Z0-9]+/$")

    for log in logs:
        if parent.match(log):
            if depth > 0:
                depth -= 1
        elif child.match(log):
            depth += 1

    return depth


