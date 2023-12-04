# Largest 3-Same-Digit Number in String
# https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/?envType=daily-question&envId=2023-12-04

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        num_tolist = [x for x in str(num)]
        largest_triplet = None

        for i in range(len(num_tolist) - 2):
            if num_tolist[i] == num_tolist[i + 1] == num_tolist[i + 2]:
                current_triplet = num_tolist[i] * 3
                if largest_triplet is None or current_triplet > largest_triplet:
                    largest_triplet = current_triplet

        return largest_triplet if largest_triplet is not None else ""
