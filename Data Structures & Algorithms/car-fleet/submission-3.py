class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        import numpy as np
        position_speed = sorted(zip(position, speed), key= lambda x : x[0], reverse=True)
        
        pos = np.array([pos for pos, _ in position_speed])
        speed = np.array([sp for _, sp in position_speed])

        stack = []

        for i in range(len(pos)):
            time = (target - pos[i])/speed[i]
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2] :
                stack.pop()

        
        return len(stack) 

            


                

            




        
        



        