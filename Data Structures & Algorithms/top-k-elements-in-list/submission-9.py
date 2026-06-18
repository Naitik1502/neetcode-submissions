class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #Time -> O(nlogn)
        #Space -> O(n)
        freq = Counter(nums)
        buckets = []
        for i in range(len(nums)+1):
            buckets.append([])
        
        print(freq)
        for elem, f in freq.items():
            buckets[f].append(elem)
        
        print(buckets)
        res = []

        for j in range(len(buckets)-1, 0, -1):
            for l in buckets[j]: 
                res.append(l)
                if len(res) >= k :
                    return res

        return res