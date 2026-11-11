class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            if nums == sorted(nums):
                return True
            if nums == sorted(nums,reverse=True):
                return True
            return False


        