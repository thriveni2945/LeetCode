from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        visit = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)

        def dfs(course):
            if visit[course] == 1:
                return False
            if visit[course] == 2:
                return True

            visit[course] = 1
            for nxt in graph[course]:
                if not dfs(nxt):
                    return False
            visit[course] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True