class Solution:
    def isBalanced(self,root):
        def f(x):
            if not x:return 0
            l,r=f(x.left),f(x.right)
            return -1 if -1 in(l,r) or abs(l-r)>1 else 1+max(l,r)
        return f(root)!=-1