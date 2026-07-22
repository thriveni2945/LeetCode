from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        left = 0
        count = len(t)
        start = 0
        length = float("inf")

        for right in range(len(s)):
            if need[s[right]] > 0:
                count -= 1
            need[s[right]] -= 1

            while count == 0:
                if right - left + 1 < length:
                    start = left
                    length = right - left + 1

                need[s[left]] += 1
                if need[s[left]] > 0:
                    count += 1
                left += 1

        if length == float("inf"):
            return ""
        return s[start:start + length]