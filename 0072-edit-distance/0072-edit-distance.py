class Solution:
    def minDistance(self,a,b):
        dp=list(range(len(b)+1))
        for i,x in enumerate(a,1):
            p=dp[0];dp[0]=i
            for j,y in enumerate(b,1):
                p,dp[j]=dp[j],p if x==y else 1+min(p,dp[j],dp[j-1])
        return dp[-1]