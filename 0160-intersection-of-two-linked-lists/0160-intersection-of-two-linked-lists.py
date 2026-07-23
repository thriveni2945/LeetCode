# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, a,b):
        x,y=a,b
        while x!=y:
            x=x.next if x else b
            y=y.next if y else a
        return x
