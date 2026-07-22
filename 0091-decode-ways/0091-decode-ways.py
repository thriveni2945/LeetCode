class Solution:
    def numDecodings(self, s: str) -> int:
        a,b=1,0
        for i,c in enumerate(s):
            t=(a if c>'0' else 0)+(b if i and "10"<=s[i-1:i+1]<="26" else 0)
            b,a=a,t
        return a
        
        