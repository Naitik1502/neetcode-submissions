class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #O(n) -> time complexity
        #O(n) -> space complexity
        n = len(nums)

        pre_fix_prod = [1]*n
        post_fix_prod = 1

        for i in range(1, n):
            pre_fix_prod[i] = nums[i-1]*pre_fix_prod[i-1]
        
        for i in range(n-2, -1, -1):
            post_fix_prod = nums[i+1]*post_fix_prod
            pre_fix_prod[i] *= post_fix_prod
            
        
        return pre_fix_prod
        