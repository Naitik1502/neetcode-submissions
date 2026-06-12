class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #BFS -> Kahn'n topological sort -> cycle detection -> false
        # Time - > O(V + E)
        # Space -> O(VE)

        # from collections import deque

        # c_map = defaultdict(int)
        # graph = defaultdict(list)


        # for c in prerequisites :
        #     a = c[0]
        #     b = c[1]
        #     c_map[b] += 1
        #     graph[a].append(b)
        
        # q = deque()

        # res = []

        # for i in range(numCourses):
        #     in_degree = c_map[i]
        #     if in_degree == 0 :
        #         q.append(i)
            
        # while q :
        #     node = q.popleft()
        #     res.append(node)

        #     for nei in graph[node]:
        #         c_map[nei] -= 1
        #         if c_map[nei] == 0 :
        #             q.append(nei)
        
        # return (len(res) == numCourses)

        #DFS 

        if not prerequisites :
           
            return True

        
        white, gray, black = 0,1,2
        graph = defaultdict(list)
        c_map = [white]*numCourses

        for c in prerequisites :
            a = c[0]
            b = c[1]
            graph[a].append(b)
        
        stack = []
    
        def dfs(node) :

            if c_map[node] == gray :
                return False 
            elif c_map[node] == black :
                return True
            
            c_map[node] = gray

            for nei in graph[node] :
                if not dfs(nei):
                    return False
                
                c_map[nei] = black
                
               
            c_map[node] = black
            stack.append(node)

            return True
        
        return all(dfs(i) for i in range(numCourses))






        