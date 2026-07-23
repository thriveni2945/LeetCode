class Solution:
    def solve(self, b):
        if not b:return
        m,n=len(b),len(b[0])
        def dfs(i,j):
            if 0<=i<m and 0<=j<n and b[i][j]=="O":
                b[i][j]="T"
                dfs(i+1,j);dfs(i-1,j);dfs(i,j+1);dfs(i,j-1)
        for i in range(m):
            dfs(i,0);dfs(i,n-1)
        for j in range(n):
            dfs(0,j);dfs(m-1,j)
        for i in range(m):
            for j in range(n):
                b[i][j]="O" if b[i][j]=="T" else "X" if b[i][j]=="O" else b[i][j]