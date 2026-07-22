class Solution:
    def simplifyPath(self, path: str) -> str:
        s=[]
        for i in path.split('/'):
            if i=='..' and s:s.pop()
            elif i not in('','.','..'):s.append(i)
        return '/'+'/'.join(s)