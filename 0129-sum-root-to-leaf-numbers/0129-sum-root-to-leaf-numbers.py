# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def f(r,v):
            if not r:return 0
            v=v*10+r.val
            if not r.left and not r.right:return v
            return f(r.left,v)+f(r.right,v)
        return f(root,0)
        