class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        a = deque()
        r = 0
        res = []

        while r < len(nums):

            num = nums[r]

            while a and r - a[0] >= k :
                a.popleft()

            while a and nums[r] > nums[a[-1]]:
                a.pop()

            a.append(r)
            if r >= k-1 :
                res.append(nums[a[0]])
            
            r = r + 1
        
        return res



        


            


        