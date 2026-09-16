import heapq
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        

    def addNum(self, num: int) -> None:
        if self.minHeap and self.minHeap[0] < num:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        while len(self.maxHeap) - len(self.minHeap) > 1:
            el = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, el)
        while len(self.minHeap) - len(self.maxHeap) > 1:
            el = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -el)
        


    def findMedian(self) -> float:
        if len(self.minHeap) != len(self.maxHeap):
            if len(self.minHeap) > len(self.maxHeap):
                return self.minHeap[0]
            else:
                return -self.maxHeap[0]

        x = self.maxHeap[0]
        y = self.minHeap[0]

        return (y - x) / 2
        
        