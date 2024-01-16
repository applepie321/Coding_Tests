# Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=daily-question&envId=2024-01-16

import random


class RandomizedSet:

    def __init__(self):
        self.data_map = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        self.data_map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not val in self.data_map:
            return False
        index = self.data_map[val]
        last_element = self.data[-1]
        self.data[index] = last_element
        self.data_map[last_element] = index
        self.data.pop()
        del self.data_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)
