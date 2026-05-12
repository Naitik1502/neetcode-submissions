class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        
        combined = sorted(zip(position, speed))

        print(combined)

        stack = []

        for p, s in combined :

            while stack and s < stack[-1][1] :

                stack_p, stack_s = stack[-1]

                dist_curr = target - p 
                dist_stack = target - stack_p

                time_curr = dist_curr/s
                time_stack = dist_stack/stack_s

                # print(time_curr)
                # print(time_stack)

                if time_curr >= time_stack:
                    stack.pop()
                else :
                    break
            
            stack.append((p,s))
        
        return len(stack)



        