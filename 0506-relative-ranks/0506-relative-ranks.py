class Solution:
    def findRelativeRanks(self, score):
        s = sorted(score, reverse=True)
        ans = []

        for x in score:
            rank = s.index(x) + 1

            if rank == 1:
                ans.append("Gold Medal")
            elif rank == 2:
                ans.append("Silver Medal")
            elif rank == 3:
                ans.append("Bronze Medal")
            else:
                ans.append(str(rank))

        return ans