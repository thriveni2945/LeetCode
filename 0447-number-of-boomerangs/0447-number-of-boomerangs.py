class Solution:
    def numberOfBoomerangs(self, points):
        ans = 0

        for i in points:
            d = {}
            for j in points:
                dist = (i[0]-j[0])**2 + (i[1]-j[1])**2
                d[dist] = d.get(dist, 0) + 1

            for c in d.values():
                ans += c * (c - 1)

        return ans