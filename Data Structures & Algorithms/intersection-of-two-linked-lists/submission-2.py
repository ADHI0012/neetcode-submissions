# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def getLen(head):
            curr = head
            count = 0
            while curr:
                count += 1
                curr = curr.next
            return count

        m,n = getLen(headA), getLen(headB)

        if m < n:
            m,n = n,m
            curr1 = headB
            curr2 = headA
        else:
            curr1 = headA
            curr2 = headB

        for _ in range(m - n):
            curr1 = curr1.next

        while curr1:
            if curr1 == curr2:
                return curr1
            curr1 = curr1.next
            curr2 = curr2.next

        return None