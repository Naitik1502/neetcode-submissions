class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)

        heap = []

        for num, freq in counter.items():
            
            heapq.heappush(heap, (freq, num))

            if len(heap) > k :
                heapq.heappop(heap)
        
        res = []

        for freq, num in heap :
            res.append(num)
        
        return res





        