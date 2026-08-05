class Solution:
    def numberToWords(self, num):
        if num == 0:
            return "Zero"

        below20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
                   "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
                   "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        def helper(n):
            if n == 0:
                return ""
            if n < 20:
                return below20[n] + " "
            if n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            return below20[n // 100] + " Hundred " + helper(n % 100)

        res = ""
        for value, name in [(1000000000, "Billion"), (1000000, "Million"), (1000, "Thousand"), (1, "")]:
            if num >= value:
                res += helper(num // value) + name + " "
                num %= value

        return res.strip()