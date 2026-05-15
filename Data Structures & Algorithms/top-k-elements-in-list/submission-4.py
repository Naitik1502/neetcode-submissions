class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        c_map = defaultdict(int)

        for num in nums:
            c_map[num] += 1

        c_map_sorted  = dict(sorted(c_map.items(), key= lambda item : item[1]))
        
        return list(c_map_sorted.keys())[-k:]

        