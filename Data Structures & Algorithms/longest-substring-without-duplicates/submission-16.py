class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #time complexity :- O(n*k) k -> len of length of the substring worst case 
        #space complexity :- O(k)

        if s == '':
            return 0
        
        # freq_map = defaultdict(int)
        # char_set = set()
        last_seen = defaultdict(int)
        # s = s.lower()

        l = 0 

        max_len = 0

        for r in range(len(s)) :
            # freq_map[s[r]] += 1
            # char_set.add(s[r])

            # while freq_map[s[r]] > 1 :
            #     freq_map[s[l]] -= 1
            #     l = l + 1
            # while s[r] in char_set :
            #     char_set.remove(s[l])
            #     l = l + 1
            # char_set.add(s[r])
            if s[r] in last_seen:
                l = max(l, last_seen[s[r]] + 1)

            last_seen[s[r]] = r
            
            max_len = max(max_len, r-l+1)
        
        return max_len
            
        