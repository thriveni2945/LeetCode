class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        max_child_depth = 0
        for child in root.children:
            max_child_depth = max(max_child_depth, self.maxDepth(child))
            
        return max_child_depth + 1