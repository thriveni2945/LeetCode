class BSTIterator:
    def __init__(self, root):
        self.a = []
        while root:
            self.a.append(root)
            root = root.left
    def next(self):
        n = self.a.pop()
        x = n.right
        while x:
            self.a.append(x)
            x = x.left
        return n.val
    def hasNext(self):
        return len(self.a) > 0