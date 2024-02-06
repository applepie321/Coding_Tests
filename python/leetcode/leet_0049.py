# Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/?envType=daily-question&envId=2024-02-06

from collections import defaultdict


def group_anagrams(strs):
    anagram_list = defaultdict(list)

    for s in strs:
        signature = ''.join(sorted(s))
        anagram_list[signature].append(s)

    return list(anagram_list.values())
