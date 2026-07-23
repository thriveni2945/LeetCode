class Solution:
    def cloneGraph(self,node):
        d={}
        def f(x):
            if not x:return
            if x in d:return d[x]
            d[x]=Node(x.val)
            d[x].neighbors=[f(n) for n in x.neighbors]
            return d[x]
        return f(node)