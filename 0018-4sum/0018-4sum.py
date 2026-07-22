from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        temp = [nums[i], nums[j], nums[left], nums[right]]
                        if temp not in result:
                            result.append(temp)
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result