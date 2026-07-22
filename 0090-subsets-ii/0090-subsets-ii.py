class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        ans = [[]]

        for num in nums:
            new = []
            for subset in ans:
                temp = subset + [num]
                if temp not in ans:
                    new.append(temp)
            ans += new

        return ans