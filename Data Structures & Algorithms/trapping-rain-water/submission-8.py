class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1

        left_max = height[0]
        right_max = height[-1]

        total = 0

        while l <= r :

            if left_max < right_max :
                total += max(left_max - height[l], 0)
                print("l", l)
                print("left_max", left_max)
                print("total", total)
                left_max = max(left_max, height[l])
                l = l + 1
            elif left_max >= right_max :
                total += max(right_max - height[r],0)
                print("r", r)
                print("r_max", right_max)
                print("total", total)
                right_max = max(right_max, height[r])
                r = r - 1
        
        return total