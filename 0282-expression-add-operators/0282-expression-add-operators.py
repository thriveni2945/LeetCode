class Solution:
    def addOperators(self, num, target):
        res = []

        def dfs(i, path, val, prev):
            if i == len(num):
                if val == target:
                    res.append(path)
                return

            for j in range(i, len(num)):
                if j > i and num[i] == '0':
                    break

                s = num[i:j+1]
                n = int(s)

                if i == 0:
                    dfs(j + 1, s, n, n)
                else:
                    dfs(j + 1, path + "+" + s, val + n, n)
                    dfs(j + 1, path + "-" + s, val - n, -n)
                    dfs(j + 1, path + "*" + s, val - prev + prev * n, prev * n)

        dfs(0, "", 0, 0)
        return res