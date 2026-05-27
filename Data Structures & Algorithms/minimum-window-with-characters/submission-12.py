class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if s == t :
            return t
        
        elif len(s) < len(t):
             return ""

        l = 0 
        
        c_map = defaultdict(int)

        window = defaultdict(int)

        for ch in t :
            c_map[ch] += 1

        have = 0
        need = len(c_map)

        # print(c_map)

        min_len = float('inf')
        final_str = ""
        
        for r, ch in enumerate(s):

            window[ch] += 1

            if ch in c_map and window[ch] == c_map[ch]:
                have += 1
            # print("Character: ", ch)
            # print("Window map: ", window)
            # print("have: ", have)
            # print("need: ", need)
            # print("r", r)
            # print("l", l)
            while have == need :
                print(s[l:r+1])
                if min_len > r - l + 1 :
                    min_len = r - l + 1
                    final_str = s[l:r+1]
                # print("final str: ", final_str)
                window[s[l]] -= 1

                if s[l] in c_map and window[s[l]] < c_map[s[l]]:
                    have -= 1

                if window[s[l]] == 0 :
                    del window[s[l]]

                
                l = l + 1
        
        return final_str
            






        