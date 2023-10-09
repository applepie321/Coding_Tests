# Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150


"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. 
Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. 
Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements 
(it's guaranteed that at least one element exists when this method is called). 
Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
"""




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