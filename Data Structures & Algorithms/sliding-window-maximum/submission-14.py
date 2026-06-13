class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque()
        

        res = []

        for n in range(len(nums)):
            
            while q and nums[q[-1]] < nums[n]:
                q.pop()
            q.append(n)
            # print(q)
            while q[0] < n + 1 - k :
                q.popleft()
            # print(q)
            if n - k + 1 >= 0 :
                res.append(nums[q[0]])
            
        return res




            

