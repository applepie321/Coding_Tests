# Determine if Two Strings Are Close
# https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=daily-question&envId=2024-01-14

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26

        for char1 in word1:
            freq1[ord(char1) - ord('a')] += 1

        for char2 in word2:
            freq2[ord(char2) - ord('a')] += 1

        for i in range(26):
            if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
                return False

        freq1.sort()
        freq2.sort()

        for i in range(26):
            if freq1[i] != freq2[i]:
                return False

        return True
