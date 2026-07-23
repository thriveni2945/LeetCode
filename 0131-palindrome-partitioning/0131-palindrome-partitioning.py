class Solution:
    def partition(self, s: str) -> List[List[str]]:
        r=[]
        def dfs(i,p):
            if i==len(s):r.append(p);return
            for j in range(i+1,len(s)+1):
                if s[i:j]==s[i:j][::-1]:
                    dfs(j,p+[s[i:j]])
        dfs(0,[])
        return r