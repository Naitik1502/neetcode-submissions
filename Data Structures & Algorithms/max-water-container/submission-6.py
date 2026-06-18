class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l<r :
            min_h = min(heights[l], heights[r])
            area = (min_h)*(r-l)
            max_area = max(area, max_area)

            if heights[l] >= heights[r]:
                r = r - 1
            else :
                l = l + 1
        
        return max_area