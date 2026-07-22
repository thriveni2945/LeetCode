# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small=[]
        large=[]
        while head:
            if head.val<x:
                small.append(head.val)
            else:
                large.append(head.val)
            head=head.next
        dummy=ListNode(0)
        cur=dummy
        for i in small+large:
            cur.next=ListNode(i)
            cur=cur.next
        return dummy.next