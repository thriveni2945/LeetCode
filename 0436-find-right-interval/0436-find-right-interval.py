import bisect

class Solution:
    def findRightInterval(self, intervals):
        starts = sorted((x[0], i) for i, x in enumerate(intervals))
        ans = []

        for s, e in intervals:
            idx = bisect.bisect_left(starts, (e,))
            if idx == len(starts):
                ans.append(-1)
            else:
                ans.append(starts[idx][1])

        return ans