# 1091. Shortest Path in Binary Matrix

# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.



# Example 1:

# Input: grid = [[0,1],[1,0]]
# Output: 2


# Example 2:

# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4


# Example 3:
# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1



# https://leetcode.com/problems/shortest-path-in-binary-matrix/solutions/3584004/python-java-c-simple-solution-easy-to-understand/


class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        queue = [(0, 0, 1)]
        grid[0][0] = 1

        for i, j, d in queue:
            if i == n - 1 and j == n - 1:
                return d

            directions = [
                (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                (i, j - 1), (i, j + 1),
                (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
            ]

            for x, y in directions:
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    grid[x][y] = 1
                    queue.append((x, y, d + 1))

        return -1
    


# The problem can be solved using a breadth-first search (BFS) algorithm.  
# We can use a queue to explore the grid cells in a breadth-first manner, starting from the top-left cell.
# At each step, we consider the neighboring cells that are valid and not visited yet, marking them as visited and adding them to the queue.
#  We continue this process until we reach the bottom-right cell or exhaust all possible paths.

