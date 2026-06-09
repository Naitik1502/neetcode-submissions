class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights) - 1
        l = 0
        r = n 

        max_area = -1*float('inf')

        while l < r :
            h_l = heights[l]
            h_r = heights[r]

            area = min(h_l,h_r)*(r - l)

            max_area = max(area, max_area)
            # print("left ", l)
            # print("right ", r)
            # print("h[l] ", h_l)
            # print("h[r] ", h_r)
            # print("area ", area)
            # print("max_area ", max_area)

            if h_l > h_r:
                r = r - 1
            else :
                l = l + 1
        
        return int(max_area)
 
