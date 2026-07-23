class Solution:
    def longestConsecutive(self, nums):
        s,ans=set(nums),0
        for n in s:
            if n-1 not in s:
                c=1
                while n+c in s:c+=1
                ans=max(ans,c)
        return ans