class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0 
        n = len(s)

        window = defaultdict(int)

        ans = 0

        for r, ch in enumerate(s):
            window[ch] += 1

            while max(window.values()) > 1 :
                l_ch = s[l]
                window[l_ch] -= 1
                if window[l_ch] == 0 :
                    del window[l_ch]
                
                l = l + 1
            
            ans = max(r-l+1, ans)
        
        return ans


