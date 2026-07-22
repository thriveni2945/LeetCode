class Solution:
    def combinationSum(self, candidates, target):
        ans = []

        def dfs(remain, path, start):
            if remain == 0:
                ans.append(path)
                return
            if remain < 0:
                return

            for i in range(start, len(candidates)):
                dfs(remain - candidates[i], path + [candidates[i]], i)

        dfs(target, [], 0)
        return ans