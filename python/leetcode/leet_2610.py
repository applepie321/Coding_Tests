# Convert an Array Into a 2D Array With Conditions
# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/?envType=daily-question&envId=2024-01-02

class Solution:
    def findMatrix(self, v: list[int]) -> list[list[int]]:
        um = {}
        for i in v:
            um[i] = um.get(i, 0) + 1

        ans = []
        while um:
            temp = []
            to_erase = []
            for f, s in um.items():
                temp.append(f)
                s -= 1
                if s == 0:
                    to_erase.append(f)
                um[f] = s
            ans.append(temp)
            for i in to_erase:
                del um[i]
        return ans
