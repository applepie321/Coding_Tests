# Maximum Difference Between Node and Ancestor
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/?envType=daily-question&envId=2024-01-11

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        distance = [0]
        self.dfs(root, distance)
        return distance[0]

    def dfs(self, root, distance):
        if not root:
            return float('inf'), float('-inf')

        left = self.dfs(root.left, distance)
        right = self.dfs(root.right, distance)

        min_val = min(root.val, min(left[0], right[0]))
        max_val = max(root.val, max(left[1], right[1]))

        distance[0] = max(distance[0], max(
            abs(min_val - root.val), abs(max_val - root.val)))

        return min_val, max_val
