# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        values = []

        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        l, r = 0, len(values) - 1
        t = True

        curr = head

        while curr:
            if t:
                curr.val = values[l]
                l += 1
            else:
                curr.val = values[r]
                r -= 1
            t = not t
            curr = curr.next

        


        
        