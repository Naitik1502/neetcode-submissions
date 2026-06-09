class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_max = [0]*len(height)
        right_max = [0]*len(height)

        running_left_max = 0 
        running_right_max = 0
        area = 0

        for i in range(0, len(height)):

            left_max[i] = running_left_max
            if height[i] > running_left_max :
                running_left_max = height[i]
        
        for i in range(len(height)-1,-1,-1 ):

            right_max[i] = running_right_max
            area += max(min(left_max[i], running_right_max) - height[i], 0)
            if height[i] > running_right_max :
                running_right_max = height[i]
        
        # print(left_max)
        # print(right_max)
        
        
        return area



            


