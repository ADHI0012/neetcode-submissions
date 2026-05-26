# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        node_before = dummy
        curr = head

        for _ in range(left - 1):
            node_before = curr
            curr = curr.next

        reverse_count = right - left + 1

        prev = None

        for _ in range(reverse_count):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        node_before.next.next = curr
        node_before.next = prev

        return dummy.next

        
