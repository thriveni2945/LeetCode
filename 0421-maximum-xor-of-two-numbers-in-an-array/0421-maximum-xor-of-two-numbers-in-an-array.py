class Solution:
    def findMaximumXOR(self, nums):
        ans = 0
        mask = 0

        for i in range(31, -1, -1):
            mask |= (1 << i)
            s = {num & mask for num in nums}
            temp = ans | (1 << i)

            for prefix in s:
                if (temp ^ prefix) in s:
                    ans = temp
                    break

        return ans