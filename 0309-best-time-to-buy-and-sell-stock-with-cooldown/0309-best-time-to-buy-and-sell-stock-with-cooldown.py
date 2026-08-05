class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        buy = -prices[0]
        sell = 0
        cool = 0

        for p in prices[1:]:
            buy, sell, cool = max(buy, cool - p), max(sell, buy + p), sell

        return max(sell, cool)