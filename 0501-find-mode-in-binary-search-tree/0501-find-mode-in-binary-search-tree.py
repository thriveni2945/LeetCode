# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root):
        values = []

        def dfs(node):
            if not node:
                return
            values.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        ans = []
        max_count = 0

        for x in set(values):
            c = values.count(x)
            if c > max_count:
                max_count = c
                ans = [x]
            elif c == max_count:
                ans.append(x)

        return ans