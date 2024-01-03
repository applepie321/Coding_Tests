# Number of Laser Beams in Bank
# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/?envType=daily-question&envId=2024-01-02

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        i = 0
        for j in bank:
            counter = j.count('1')
            if counter:
                result += i * counter
                i = counter
        return result
