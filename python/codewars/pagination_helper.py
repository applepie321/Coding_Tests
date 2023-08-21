# PaginationHelper
# https://www.codewars.com/kata/515bb423de843ea99400000a/solutions/python


# For this exercise you will be strengthening your page-fu mastery. 
# You will complete the PaginationHelper class, which is a utility class 
# helpful for querying paging information related to an array.

# The class is designed to take in an array of values and an integer indicating 
# how many items will be allowed per each page. 
# The types of values contained within the collection/array are not relevant.

# The following are some examples of how this class is used:


class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
    
    def item_count(self):
        return len(self.collection)
    
    def page_count(self):
        return (len(self.collection) + self.items_per_page - 1) // self.items_per_page
    
    def page_item_count(self, page_index):
        if page_index < 0 or page_index >= self.page_count():
            return -1
        elif page_index == self.page_count() - 1:
            return len(self.collection) % self.items_per_page or self.items_per_page
        else:
            return self.items_per_page
    
    def page_index(self, item_index):
        if item_index < 0 or item_index >= len(self.collection):
            return -1
        else:
            return item_index // self.items_per_page
        



# Best practice

class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self._item_count = len(collection)
        self.items_per_page = items_per_page

    def item_count(self):
        return self._item_count

    def page_count(self):
        return -(self._item_count // -self.items_per_page)

    def page_item_count(self, page_index):
        return min(self.items_per_page, self._item_count - page_index * self.items_per_page) \
            if 0 <= page_index < self.page_count() else -1

    def page_index(self, item_index):
        return item_index // self.items_per_page \
            if 0 <= item_index < self._item_count else -1