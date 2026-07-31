class Solution:
    def reverseWords(self, s: str) -> str:
        # Split by spaces, reverse each word, and join them back
        return " ".join(word[::-1] for word in s.split())