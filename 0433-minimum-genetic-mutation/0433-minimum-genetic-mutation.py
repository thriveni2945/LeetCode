from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1

        q = deque([(startGene, 0)])
        genes = ['A', 'C', 'G', 'T']
        visited = {startGene}

        while q:
            gene, steps = q.popleft()

            if gene == endGene:
                return steps

            for i in range(len(gene)):
                for ch in genes:
                    new = gene[:i] + ch + gene[i+1:]
                    if new in bank and new not in visited:
                        visited.add(new)
                        q.append((new, steps + 1))
        return -1