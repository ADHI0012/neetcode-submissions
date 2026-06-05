# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        carry = 0

        while l1 and l2:
            res = l1.val + l2.val + carry
            if res >= 10:
                carry = 1
                res = res % 10
            else:
                carry = 0
            temp.next = ListNode(res)
            l1 = l1.next
            l2 = l2.next
            temp = temp.next

        while l1:
            res = l1.val + carry
            if res >= 10:
                carry = 1
                res = res % 10
            else:
                carry = 0
            temp.next = ListNode(res)
            l1 = l1.next
            temp = temp.next

        while l2:
            res = l2.val + carry
            if res >= 10:
                carry = 1
                res = res % 10
            else:
                carry = 0
            temp.next = ListNode(res)
            l2 = l2.next
            temp = temp.next

        if carry:
            temp.next = ListNode(carry)
        return dummy.next

