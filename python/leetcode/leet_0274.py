# leet_0274 : H-index
# https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150



# Given an array of integers citations where citations[i] is the number of citations 
# a researcher received for their ith paper, return the researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined 
# as the maximum value of h such that the given researcher has published 
# at least h papers that have each been cited at least h times.




# https://leetcode.com/problems/h-index/solutions/3602383/explained-simple-and-clear-python3-code/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def hIndex(self, c: List[int]) -> int:
        c.sort(reverse=True)
        if len(c)==1 and c[0]>0:
            return 1
        if c[-1]>=len(c):
            return len(c)
        for i in range(len(c)):
            if c[i]<i+1:
                return i
        return 0
    



# https://leetcode.com/problems/h-index/submissions/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        h = 0

        if n == 1 and citations[0] == 0:
            return 0
        else:
            for i in range(n):
                if citations[i] < n - i:
                   h = citations[i]
                else:
                    h = max(h, n-i)
            return h