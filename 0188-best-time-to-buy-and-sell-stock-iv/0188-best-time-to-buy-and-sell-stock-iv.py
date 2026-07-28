class Solution:
    def maxProfit(self, k, prices):
        if not prices or k == 0:
            return 0

        if k >= len(prices) // 2:
            profit = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        buy = [-10**9] * (k + 1)
        sell = [0] * (k + 1)

        for p in prices:
            for i in range(1, k + 1):
                buy[i] = max(buy[i], sell[i - 1] - p)
                sell[i] = max(sell[i], buy[i] + p)

        return sell[k]