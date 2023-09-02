class RandomizedSet:

    def __init__(self):
        self.data_map = {}
        self.data = []
        

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        self.data.append(val)
        

    def remove(self, val: int) -> bool:
        if not val in self.data_map:
            return False
        
        lat_item_in_list = selfa.data[-1]
        index_of_item_to_remove = self.data_map[val]

        self.data_map[last_item_in_list] = index_of_item_to_remove
        self.data[index_of_item_to_remove] = last_item_in_list
        

    def getRandom(self) -> int:
    