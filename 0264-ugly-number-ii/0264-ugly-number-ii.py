class Solution:
    def nthUglyNumber(self, n):
        ugly = [1]
        i2 = i3 = i5 = 0

        while len(ugly) < n:
            a = ugly[i2] * 2
            b = ugly[i3] * 3
            c = ugly[i5] * 5

            x = min(a, b, c)
            ugly.append(x)

            if x == a:
                i2 += 1
            if x == b:
                i3 += 1
            if x == c:
                i5 += 1

        return ugly[-1]