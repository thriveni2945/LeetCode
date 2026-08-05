class Solution:
    def compress(self, chars):
        s = []
        i = 0

        while i < len(chars):
            ch = chars[i]
            count = 1

            while i + 1 < len(chars) and chars[i] == chars[i + 1]:
                count += 1
                i += 1

            s.append(ch)
            if count > 1:
                for c in str(count):
                    s.append(c)
            i += 1

        chars[:] = s
        return len(chars)