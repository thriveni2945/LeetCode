class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        q = deque([(beginWord, 1)])
        while q:
            w, d = q.popleft()
            if w == endWord:
                return d
            for i in range(len(w)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nw = w[:i] + c + w[i+1:]
                    if nw in wordList:
                        wordList.remove(nw)
                        q.append((nw, d + 1))
        return 0