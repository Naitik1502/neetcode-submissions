class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = {}

        l = 0

        max_len = 0
        
        for r in range(len(s)):

            if s[r] in char_set:
                l = max(char_set[s[r]]+1, l)
            
            char_set[s[r]] = r

            max_len = max(max_len, r - l + 1)
        
        return max_len

        