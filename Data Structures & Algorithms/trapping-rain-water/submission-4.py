class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)

        left_max = height[0]
        right_max = height[-1]

        l = 0
        r = n - 1

        total = 0

        while l < r :
           
            if left_max < right_max :
                l = l + 1
                left_max = max(left_max, height[l])
                total += left_max - height[l]
            else : 
                r = r - 1
                right_max = max(right_max, height[r])
                total += right_max - height[r]
    
        return total
            
