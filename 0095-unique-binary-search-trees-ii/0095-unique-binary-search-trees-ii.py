# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []

        def dfs(l, r):
            if l > r:
                return [None]

            res = []
            for i in range(l, r + 1):
                for left in dfs(l, i - 1):
                    for right in dfs(i + 1, r):
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res

        return dfs(1, n)