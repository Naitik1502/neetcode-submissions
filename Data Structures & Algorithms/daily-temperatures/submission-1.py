class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        answer = [0]*len(temperatures)

        for i, temp in enumerate(temperatures):
            if not stack :
                stack.append(i)
            elif temp > temperatures[stack[-1]] :
                while stack and temp > temperatures[stack[-1]]:
                    index = stack.pop()
                    answer[index] = i - index
                stack.append(i)
            else :
                stack.append(i)
        
        return answer