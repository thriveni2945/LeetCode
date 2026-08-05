# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node,path):
            if not node:
                return 0
            path=[x+node.val for x in path]+[node.val]
            count=path.count(targetSum)
            return count+dfs(node.left,path)+dfs(node.right,path)
        return dfs(root,[])
        
        