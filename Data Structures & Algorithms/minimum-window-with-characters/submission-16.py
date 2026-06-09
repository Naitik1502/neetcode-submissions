class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""
        
        freq_map = Counter(t)
        need_char = len(freq_map)
        have = 0

        min_res = [float('inf'),-1,-1]

        l = 0 
        window_map = defaultdict(int)

        for r, r_ch in enumerate(s):
            window_map[r_ch] += 1

            if r_ch in freq_map and freq_map[r_ch] == window_map[r_ch]:
                have += 1
            
            # print(need_char)
            print(have)
            while need_char == have and l <= r :
                l_ch = s[l]
                window_map[l_ch] -= 1
                print(s[l:r+1])
                print(l)
                print(r)
                if r - l + 1 < min_res[0]:
                    min_res[0] = r - l + 1
                    min_res[1] = l 
                    min_res[2] = int(r)

                if l_ch in freq_map and window_map[l_ch] < freq_map[l_ch]:
                    have -= 1
                  
                
                if window_map[l_ch] == 0 :
                    del window_map[l_ch]
                
                l += 1
        
        return s[min_res[1]: min_res[2]+1]
            



            


