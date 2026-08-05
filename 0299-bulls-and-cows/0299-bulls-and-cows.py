class Solution:
    def getHint(self, secret, guess):
        bulls = cows = 0
        s = {}
        g = {}

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                s[secret[i]] = s.get(secret[i], 0) + 1
                g[guess[i]] = g.get(guess[i], 0) + 1

        for k in s:
            if k in g:
                cows += min(s[k], g[k])

        return str(bulls) + "A" + str(cows) + "B"