class PeekingIterator:
    def __init__(self, iterator):
        self.it = iterator
        self.nextVal = iterator.next() if iterator.hasNext() else None

    def peek(self):
        return self.nextVal

    def next(self):
        val = self.nextVal
        self.nextVal = self.it.next() if self.it.hasNext() else None
        return val

    def hasNext(self):
        return self.nextVal is not None