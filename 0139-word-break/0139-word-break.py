class Solution:
    def wordBreak(self, s, wordDict):
        dp = [True] + [False] * len(s)
        w = set(wordDict)
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in w:
                    dp[i] = True
                    break
        return dp[-1]