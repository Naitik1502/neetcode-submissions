class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)

        print(nums)
        l = 0

        ans = []

        for k, num in enumerate(nums):

            if k > 0 and nums[k] == nums[k-1]:
                continue

            target = -1*num 

            l = k + 1
            r = len(nums) - 1

            while l < r :
                # print(l)
                # print(r)
                # print(nums[l]+nums[r])
                # print(nums[k])

                # break

                if l == k :
                    l = l + 1
                    continue
                if r == k :
                    r = r - 1 
                    continue
                
                if nums[l] + nums[r] == target :
                    ans.append([nums[l],nums[r],nums[k]])
                    print([nums[l],nums[r],nums[k]])
                    l = l + 1
                    while l > 0 and l < len(nums) - 1 and nums[l] == nums[l-1]:
                        l = l + 1
        
                if nums[l] + nums[r] < target:
                    l = l + 1
                    while l > 0 and nums[l] == nums[l-1]:
                        l = l + 1
                if nums[l] + nums[r] > target:
                    r = r - 1
                    while r < len(nums) - 1 and r > -1 and nums[r] == nums[r+1]:
                        r = r - 1
                
                # print(l)
                # print(r)
                # print(nums[l]+nums[r])
                # print(nums[k])
       
        return ans
                    
                
                





        