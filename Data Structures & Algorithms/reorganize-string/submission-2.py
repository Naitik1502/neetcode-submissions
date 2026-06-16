from _heapq import heapify
class Solution:
    def reorganizeString(self, s: str) -> str:

        #Time -> O(nlogn)
        #Space -> O(n)
        
        ch_map = [(-v,k) for k, v in Counter(s).items()]
        heapq.heapify(ch_map)
       
        ans = []
        prev = None
       
        while ch_map :
            new_freq, new_char = heapq.heappop(ch_map)
        
            if prev :
                heapq.heappush(ch_map, prev)
                
    
            ans.append(new_char)
            new_freq += 1
            
            
            if new_freq < 0 :
                prev = (new_freq, new_char)
            else :
                prev = None
            
            

        return "".join(ans) if len(ans) == len(s) else ""
        
    
        