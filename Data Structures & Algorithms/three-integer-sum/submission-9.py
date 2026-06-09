class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        res = []

        for k in range(len(nums)):
            if k > 0 and nums[k-1] == nums[k] :
                continue
            l = k + 1
            r = len(nums) - 1

            while l < r :

                if nums[k] + nums[l] + nums[r] == 0 :
                    res.append([nums[k], nums[l], nums[r]])
                    # print(nums)
                    # print((k,l,r))
                    l += 1
                    r -= 1
                    while l < r and nums[l-1] == nums[l] :
                        l += 1
                    while l < r < len(nums) - 1 and nums[r] == nums[r+1] :
                        r -= 1
                elif nums[k] + nums[l] + nums[r] < 0 :
                    # print(nums[l-1])
                    # print(nums[l])
                    # print("#")
                    if nums[l-1] == nums[l] :
                        while l < r and nums[l-1] == nums[l] :
                            l += 1
                    else :
                        l += 1
                    
                        # print("left duplicate removal")
                    
                
                elif nums[k] + nums[l] + nums[r] > 0 :
                    
                    if r < len(nums) - 1 and nums[r] == nums[r+1]:
                        while l < r < len(nums) - 1 and nums[r] == nums[r+1] :
                            r -= 1
                    else :
                        r -=1 
                    
                    
        
        return res
                    
                

