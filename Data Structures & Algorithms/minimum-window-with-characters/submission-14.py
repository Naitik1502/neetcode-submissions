class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t) :
            return ""

        t_map = defaultdict(int)

        for ch in t :
            t_map[ch] += 1 
        
        have = 0 
        need = len(t_map)

        window = defaultdict(int)

        l = 0

        min_len = float('inf')
        final_ans = ""

        for r, r_ch in enumerate(s):

            window[r_ch] += 1

            if r_ch in t_map and window[r_ch] == t_map[r_ch] :
                have += 1
            
            while have == need :

                sub_len = r-l+1

                final_ans = s[l:r+1] if sub_len < min_len else final_ans
                min_len = min(sub_len, min_len)
                l_ch = s[l]
                window[l_ch] -= 1

                if l_ch in t_map and window[l_ch] < t_map[l_ch] :
                    have -= 1
                
                if window[l_ch] == 0 :
                    del window[l_ch]
                
                l += 1
        

        return final_ans



        
        