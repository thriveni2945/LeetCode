class Solution:
    def restoreIpAddresses(self,s):
        r=[]
        def f(i,p,a):
            if p==4:return i==len(s) and r.append(a[:-1])
            for j in range(1,4):
                if i+j<=len(s) and (j==1 or s[i]!='0') and int(s[i:i+j])<256:
                    f(i+j,p+1,a+s[i:i+j]+'.')
        f(0,0,"")
        return r