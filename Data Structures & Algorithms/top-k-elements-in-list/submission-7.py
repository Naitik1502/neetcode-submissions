class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)

        buckets = [ [] for _ in range(len(nums)+ 1)]
       

        for key,v in counter.items():
          
            buckets[v].append(key)
            
            
        
       
        res = []

        for i in range(len(buckets)-1, -1, -1):
           
            if len(res) == k:
                return res
            res.extend(buckets[i])
        
        return 
            




        