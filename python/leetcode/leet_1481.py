# Least Number of Unique Integers after K Removals
# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/?envType=daily-question&envId=2024-02-16

from collections import Counter


def find_least_num_of_unique_ints(arr, k) -> int:
    counter = Counter(arr)
    sorted_counts = sorted(counter.values())
    removed_elements = 0

    for i in range(len(sorted_counts)):
        removed_elements += sorted_counts[i]
        if removed_elements > k:
            return len(sorted_counts) - i

    return 0
