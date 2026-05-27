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
        currA = headA
        currB = headB

        if m > n:
            for _ in range(m - n):
                currA = currA.next
        else:
            for _ in range(n - m):
                currB = currB.next

        while currB:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next

        return None