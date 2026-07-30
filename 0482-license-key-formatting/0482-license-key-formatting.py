class Solution:
    def licenseKeyFormatting(self, s, k):
        s = s.replace("-", "").upper()
        ans = ""

        while len(s) > k:
            ans = "-" + s[-k:] + ans
            s = s[:-k]

        return s + ans