# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            itr = curr.next
            curr.next = prev
            prev = curr
            curr = itr
        
        f = head
        while prev:
            curr1,curr2 = f.next, prev.next
            f.next = prev
            prev.next = curr1
            f , prev = curr1,curr2
