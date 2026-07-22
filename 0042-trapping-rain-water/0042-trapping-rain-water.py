class Solution:
    def trap(self, height):
        l, r = 0, len(height)-1
        lm = rm = ans = 0
        while l < r:
            if height[l] < height[r]:
                lm = max(lm, height[l])
                ans += lm - height[l]
                l += 1
            else:
                rm = max(rm, height[r])
                ans += rm - height[r]
                r -= 1
        return ans