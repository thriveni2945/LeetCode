class Solution:
    def isAdditiveNumber(self, num):

        def dfs(a, b, s):
            if not s:
                return True
            c = str(int(a) + int(b))
            return s.startswith(c) and dfs(b, c, s[len(c):])

        n = len(num)

        for i in range(1, n):
            for j in range(i + 1, n):
                a = num[:i]
                b = num[i:j]

                if (a.startswith("0") and len(a) > 1) or (b.startswith("0") and len(b) > 1):
                    continue

                if dfs(a, b, num[j:]):
                    return True

        return False