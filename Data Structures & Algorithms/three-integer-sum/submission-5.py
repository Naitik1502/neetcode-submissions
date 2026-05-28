class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        print(nums)
        res = []

        for k in range(len(nums)):

            if k > 0 and nums[k] == nums[k-1]:
                continue

            l = k + 1
            r = len(nums) - 1

            target = -1*nums[k]

            while l < r :

                two_sum = nums[l] + nums[r]
                # print("Two sum: ", two_sum)
                # print("l: ",l)
                # print("r: ",r)
                # print("nums[l]: ", nums[l])
                # print("nums[r]: ", nums[r])
                # print("target: ",target)
                # print("#")

                if two_sum < target :
                    l = l + 1
                    while 0 < l < r and nums[l] == nums[l-1]:
                        l = l + 1
                elif two_sum == target :
                    res.append([nums[l], nums[k], nums[r]])
                    l = l + 1
                    while 0 < l < r and nums[l] == nums[l-1]:
                        l = l + 1
                    r = r - 1
                    while l < r < len(nums) - 1 and nums[r] == nums[r+1]:
                        r = r - 1

                elif two_sum > target :
                    r = r - 1
                    while l < r < len(nums) - 1 and nums[r] == nums[r+1]:
                        r = r - 1
            
        return res




        