# Maximum Length of a Concatenated String with Unique Characters
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/?envType=daily-question&envId=2024-01-23

# DFS
class Depth_First_Search:
    def max_length(self, arr):
        result = [0]
        self.dfs(arr, "", 0, result)
        return result[0]

    def dfs(self, arr, path, idx, result):
        if self.is_unique_chars(path):
            result[0] = max(result[0], len(path))

        if idx == len(arr) or not self.is_unique_chars(path):
            return

        for i in range(idx, len(arr)):
            self.dfs(arr, path+arr[i], i+1, result)

    def is_unique_chars(self, s):
        char_set = set()
        for char in s:
            if char in char_set:
                return False
            char_set.add(char)
        return True


# arr = array
# idx = index
# s = string
