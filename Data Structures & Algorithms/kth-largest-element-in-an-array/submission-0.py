class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        res = []

        for i, num in enumerate(nums):
            heapq.heappush(res, -num)
        
        
        while k :
            ans = heapq.heappop(res)
            k -= 1
        
        return ans*-1