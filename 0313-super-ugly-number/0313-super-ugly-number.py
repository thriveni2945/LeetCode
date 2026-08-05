import heapq

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        heap = [1]
        seen = {1}

        for _ in range(n):
            ugly = heapq.heappop(heap)
            for p in primes:
                x = ugly * p
                if x not in seen:
                    seen.add(x)
                    heapq.heappush(heap, x)

        return ugly