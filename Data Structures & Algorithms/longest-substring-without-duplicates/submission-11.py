class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #time complexity :- O(n*k) k -> len of length of the substring worst case 
        #space complexity :- O(n)

        if s == '':
            return 0
        
        freq_map = defaultdict(int)
        # s = s.lower()

        l = 0 

        max_len = 0

        for r in range(len(s)) :
            freq_map[s[r]] += 1

            while max(freq_map.values()) > 1 :
                ch_out = s[l]
                freq_map[s[l]] -= 1
                l = l + 1
            
            max_len = max(max_len, r-l+1)
        
        return max_len
            
        