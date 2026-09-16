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

        for i in range(n):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        while heap:
            value, index = heapq.heappop(heap)
            curr.next = ListNode(value)
            curr = curr.next
            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(heap, (lists[index].val, index))
        
        return dummy.next


        # while heap:
        #     curr.next = ListNode(heapq.heappop(heap))
        #     curr = curr.next
        

            
        
        return dummy.next
                
            