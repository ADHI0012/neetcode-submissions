class MedianFinder:

    def __init__(self):
        self.data = []
        

    def addNum(self, num: int) -> None:
        self.data.append(num)
        

    def findMedian(self) -> float:
        n = len(self.data)
        self.data.sort()
        if n % 2:
            return self.data[n // 2]
        
        median = (self.data[n // 2] + self.data[(n // 2) - 1]) / 2
        return median

        
        