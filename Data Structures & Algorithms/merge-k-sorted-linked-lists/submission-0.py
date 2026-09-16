# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode(0)
        curr = dummy
        n = len(lists)
        if n == 0: return None

        while True:
            flag = False
            for i in range(n):
                if lists[i]:
                    flag = True
                    heapq.heappush(heap, lists[i].val)
                    lists[i] = lists[i].next
            if not flag:
                break
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next

        while heap:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next
        

            
        
        return dummy.next
                
            