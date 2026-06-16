class MedianFinder:

    def __init__(self):
        self.arr = []
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:

        
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        

    def findMedian(self) -> float:
 
        if len(self.max_heap) >  len(self.min_heap) :
            elem = -self.max_heap[0]
            return elem
        else :
            print((self.min_heap[0] + -1*self.max_heap[0])/2)
            return (self.min_heap[0] + -1*self.max_heap[0])/2
        

        
        