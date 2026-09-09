# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head :
            return
        a = []
        curr = head
        while curr:
            a.append(curr)
            curr = curr.next
        
        i,j = 0, len(a)-1
        while i<j:
            a[i].next = a[j]
            i+=1
            if i>=j:
                break
            a[j].next = a[i]
            j-=1
        a[i].next = None

    