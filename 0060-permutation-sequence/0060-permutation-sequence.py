class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial

        nums = []
        for i in range(1, n + 1):
            nums.append(str(i))

        k -= 1
        ans = ""

        for i in range(n, 0, -1):
            f = factorial(i - 1)
            index = k // f
            ans += nums[index]
            nums.pop(index)
            k %= f

        return ans