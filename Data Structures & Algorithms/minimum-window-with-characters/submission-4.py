class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t) :
            return ""

        t_count_map = Counter(t)

        have_ch = 0
        need_ch = len(t_count_map)
        l = 0

        sub_str_map = defaultdict(int)

        min_len = 10000
        res = None

        for r, ch in enumerate(s):

            sub_str_map[ch] += 1

            if ch in t_count_map and sub_str_map[ch] == t_count_map[ch]:
                have_ch += 1

            # print(sub_str_map)
            # print(have_ch)
            while need_ch == have_ch:
                if r-l + 1 < min_len :
                    res = (l,r)
                    min_len = r - l + 1
    
                sub_str_map[s[l]] -= 1
                if s[l] in t_count_map and sub_str_map[s[l]] < t_count_map[s[l]]:
                    have_ch -= 1
                l = l + 1
            # print(res)
        
        # print(res)
        return s[res[0]:res[1]+1] if res else  ""

            

                


            






        