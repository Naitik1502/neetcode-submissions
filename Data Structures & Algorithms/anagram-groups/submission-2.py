class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        str_map = {}

        for i, s in enumerate(strs):
            # print(s)
            if ''.join(sorted(s)) in str_map :
                # print("in map")
                # print(s)
                str_map[''.join(sorted(s))].append(s)
            else :
                # print("out map")
                # print(s)
                str_map[''.join(sorted(s))] = []
                str_map[''.join(sorted(s))].append(s)
            
            # print(str_map)
        

        res = []

        for k in str_map.keys():
            res.append(str_map[k])
        
        return res
            

        