# Leaf-Similar Trees
# https://leetcode.com/problems/leaf-similar-trees/?envType=daily-question&envId=2024-01-09

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.get_leaf_nodes(root1) == self.get_leaf_nodes(root2)

    def get_leaf_nodes(self, root):
        if root is None:
            return []
        leaf_nodes = []

        def dfs(node):
            if node is None:
                return
            if node.left is None and node.right is None:
                leaf_nodes.append(node.val)
                return
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return leaf_nodes
