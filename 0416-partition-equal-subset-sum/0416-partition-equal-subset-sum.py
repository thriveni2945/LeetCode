class Solution:
    def canPartition(self, nums):
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        dp = {0}

        for num in nums:
            dp |= {x + num for x in dp if x + num <= target}

        return target in dp