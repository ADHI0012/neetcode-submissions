# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        values = []
        curr = head
        dummy = ListNode()
        
        while curr:
            if curr.val != val:
                values.append(curr.val)
            curr = curr.next

        newHead = dummy

        for value in values:
            newHead.next = ListNode(value)
            newHead = newHead.next

        return dummy.next

        

        