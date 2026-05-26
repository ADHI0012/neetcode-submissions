# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        sec = slow.next
        prev = None

        while sec:
            next_node = sec.next
            sec.next = prev
            prev = sec
            sec = next_node

        sec = prev
        slow.next = sec

        curr = head

        while sec:
            if curr.val != sec.val:
                return False
            sec = sec.next
            curr = curr.next

        return True
            