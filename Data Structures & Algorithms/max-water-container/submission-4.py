class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0 

        r = len(heights) - 1

        max_area = 0

        while l < r :

            l_h = heights[l]
            r_h = heights[r]

            curr_area = min(l_h, r_h)*(r - l)

            print(l)
            print(r)

            print(curr_area)

            max_area = max(curr_area, max_area)

            if l_h < r_h :
                l = l + 1
            elif l_h >= r_h :
                r = r - 1
        
        return max_area


        