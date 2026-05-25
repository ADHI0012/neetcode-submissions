# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        l = left - 1
        r = right - 1

        while l < r:
            values[l], values[r] = values[r], values[l]
            l, r = l + 1, r - 1

        curr = head
        i = 0
        while curr:
            curr.val = values[i]
            i += 1
            curr = curr.next

        return head

        
