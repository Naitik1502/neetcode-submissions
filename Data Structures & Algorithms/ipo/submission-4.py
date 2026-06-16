class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #Time -> O(nlogn)
        #Space -> O(n)
        capital_heap = []
        for i, c in enumerate(capital):
            heapq.heappush(capital_heap, (c, profits[i], i))
        
        profit_heap = []
        while k :    
            while capital_heap and w >= capital_heap[0][0]:
                min_cap, prof, i = heapq.heappop(capital_heap)
                heapq.heappush(profit_heap,-prof)
                
                
            if not profit_heap :
                return w

            prof = heapq.heappop(profit_heap)
            w += abs(prof)
            k -= 1
        
        return w
            

            


        