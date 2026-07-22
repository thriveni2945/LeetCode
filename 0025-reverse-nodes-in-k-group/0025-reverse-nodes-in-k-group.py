# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        values = []

        while head:
            values.append(head.val)
            head = head.next

        for i in range(0, len(values), k):
            if i + k <= len(values):
                values[i:i + k] = reversed(values[i:i + k])

        dummy = ListNode(0)
        curr = dummy

        for val in values:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next 