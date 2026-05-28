class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        left_max_arr = [0]*n
        right_max_arr = [0]*n

        left_max = height[0]
        right_max = height[-1]

        for i, h in enumerate(height):

            if i == 0 :
                continue
                # left_max = h
            
            left_max_arr[i] = left_max

            if h > left_max :
                left_max = h 
        
        for j in range(n - 1, -1, -1):
            h = height[j]
            if j == n - 1 :
                continue
                # right_max = height[j]       
            right_max_arr[j] =  right_max

            if h > right_max :
                right_max = h
            
        
        rain_water = 0

        for k in range(len(height)):
            rain_water += max(min(left_max_arr[k], right_max_arr[k]) - height[k], 0)
        
    
        return rain_water
            
