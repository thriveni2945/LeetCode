class Solution:
    def removeInvalidParentheses(self, s):
        level = {s}

        while True:
            valid = [x for x in level if self.check(x)]
            if valid:
                return valid

            level = {
                x[:i] + x[i+1:]
                for x in level
                for i in range(len(x))
                if x[i] in "()"
            }

    def check(self, s):
        c = 0
        for ch in s:
            if ch == "(":
                c += 1
            elif ch == ")":
                c -= 1
                if c < 0:
                    return False
        return c == 0