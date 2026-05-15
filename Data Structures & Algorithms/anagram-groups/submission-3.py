class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        str_map = defaultdict(list)

        for s in strs:
            freq_map = [0]*26
            for ch in s :
                freq_map[ord(ch)-ord('a')] += 1
            
            key = ''.join(str(freq_map))
            str_map[key].append(s)
        
        return list(str_map.values())

        