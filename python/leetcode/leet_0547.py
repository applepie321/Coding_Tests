# 547. Number of Provinces

# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.


# Solution by peyman_np

# https://leetcode.com/problems/number-of-provinces/solutions/727759/python3-solution-with-detailed-explanation/


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)  #1
        visited = [False]*n  #2
        count = 0  #3
        
        if not M:  #4
            return 0  #5
        
        def dfs(u):  #6
            for v in range(n):  #7
                if M[u][v] == 1 and visited[v] == False:  #8
                    visited[v] = True  #9
                    dfs(v)  #10
        
        
        for idx in range(n): #11
            if visited[idx] == False: #12
                count += 1 #13
                visited[idx] == True #14
                dfs(idx) #15
        
        return count #16
    



# First note: If you hear anything regarding relationship, circle, etc., you should think of a way to interpret it as a graph.

# After you read the problem statement, try to visualize some examples as a graph on a piece of paper. 
# For example, for M = [[1,1,0], [1,1,0], [0,0,1]]. If you draw three nodes 0, 1, 2, and try to connect them in case M_{ij} is one,
#  you would connect node 0 to node 1, and node 2 would be left alon. How many connected pieces do you have? 2! right? 
# So, there are two friend cycles. That' the idea behind our solution here. 
# You try to go over all vertices (we have n vertices, which is the len(M), starting from whatever node you want! Once you start from a vertex, 
# Depth First Search (DFS) algorithm would try to visit every node that can be arrived at given a specific starting vertex. 
# The algorithm only stops if it visits all the vertices in a connected graph. Makes sense? Good! I'm following the solution of user8307e