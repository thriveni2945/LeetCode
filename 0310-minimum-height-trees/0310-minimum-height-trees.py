from collections import deque

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]

        graph = [set() for _ in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = deque(i for i in range(n) if len(graph[i]) == 1)

        while n > 2:
            size = len(leaves)
            n -= size
            for _ in range(size):
                leaf = leaves.popleft()
                nei = graph[leaf].pop()
                graph[nei].remove(leaf)
                if len(graph[nei]) == 1:
                    leaves.append(nei)

        return list(leaves)