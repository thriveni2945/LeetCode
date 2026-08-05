class Solution:
    def longestPalindrome(self, s):
        count = {}
        length = 0
        odd = False

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for value in count.values():
            length += (value // 2) * 2
            if value % 2 == 1:
                odd = True

        if odd:
            length += 1

        return length