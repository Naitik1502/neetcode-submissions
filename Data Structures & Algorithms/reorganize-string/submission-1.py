from _heapq import heapify
class Solution:
    def reorganizeString(self, s: str) -> str:
        ch_map = [0]*26
        ch_map = []
        ch_map = [(-v,k) for k, v in Counter(s).items()]
        # for ch in s :
        #     ch_map[ord(ch)-ord('a')] -= 1
            
        print(ch_map)
        heapq.heapify(ch_map)
        print(ch_map)
        ans = ""
        print("making string")
        while ch_map :
            new_freq, new_char = heapq.heappop(ch_map)
            buffer = []
            # print(ans)
            # print(ch_map)
            while len(ans) > 0 and ans[-1] == new_char :
                buffer.append((new_freq, new_char))
                # print(ch_map)
                if len(ch_map) == 0:
                    return ""
                new_freq, new_char = heapq.heappop(ch_map)
                
            
            ans += new_char
            new_freq += 1
            if new_freq < 0 :
                buffer.append((new_freq, new_char))
            
            for elem in buffer :
                heapq.heappush(ch_map, elem)


        return ans
        
    
        