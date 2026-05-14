class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2) :
            return False

        s1_map = {}
        window_map = {}

        for i, ch in enumerate(s1) :
            s1_map[ch] = 1 + s1_map.get(ch, 0)
            window_map[s2[i]] = 1 + window_map.get(s2[i], 0)
        
        if window_map == s1_map:
            return True
        
        l = 0 

        for r in range(len(s1), len(s2)):

            window_map[s2[r]] = 1 + window_map.get(s2[r], 0)

            window_map[s2[l]] -= 1

            if not  window_map[s2[l]] :
                del window_map[s2[l]]
            
            if window_map == s1_map :
                return True
            
            l = l + 1
        
        return False 

        

        
