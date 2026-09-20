# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        node_before = dummy

        for _ in range(left - 1):
            node_before = node_before.next
        
        curr = node_before.next
        prev = None
        rev_count = right - left + 1

        for i in range(rev_count):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        node_before.next.next = curr
        node_before.next = prev
        
    
        return dummy.next