class Solution:
    def countDigitOne(self, n: int) -> int:
        ans=0
        m=1
        while m<=n:
            a=n//m
            b=n%m
            ans+=(a+8)//10*m
            if a%10==1:
                ans+=b+1
            m*=10
        return ans
        
        