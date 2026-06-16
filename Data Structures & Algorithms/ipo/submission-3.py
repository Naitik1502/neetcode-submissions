class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        
        p_to_c_mapping = {}
        for i, p in enumerate(profits):
            p_to_c_mapping[i] = i
            profits[i] = profits[i]*-1
            

        capital_heap = []
        for i, c in enumerate(capital):
            heapq.heappush(capital_heap, (c, profits[i], i))
        
        profit_heap = []
        while k :
            # print(w)
            # print(k)
            # print(capital_heap[0])
            
            while capital_heap and w >= capital_heap[0][0]:
                # print("Profit heap selected")
                min_cap, prof, i = heapq.heappop(capital_heap)
                heapq.heappush(profit_heap,prof)
                # print(profits)
                prof = heapq.heappop(profits) 
                # print("profit added ", abs(prof))
                
            
                # print("capital heap selected")
            if not profit_heap :
                return w
                
            prof = heapq.heappop(profit_heap)
                # print("profits before ", profits) 
                
                # print("profits after ", profits) 
                # print("profit added ", abs(prof))
            w += abs(prof)
            k -= 1
        
        return w
            

            


        