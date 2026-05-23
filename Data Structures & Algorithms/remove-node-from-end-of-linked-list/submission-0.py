# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next

        n = count - n
        curr = head

        if n == 0:
            return head.next

        for i in range(n - 1):
            if not curr.next:
                return head
            curr = curr.next

        curr.next = curr.next.next

        return head

        
        