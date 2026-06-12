class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        from collections import deque

        #Time Complexity :- O(V+E)
        #Space Complexity :- O(V+E)

        in_degree = [0]*numCourses
        graph = defaultdict(list)
        
        for _, p in enumerate(prerequisites):
            
            graph[p[0]].append(p[1])
            in_degree[p[1]] += 1
        
        q = []
        
        for i in range(numCourses):
            if in_degree[i] == 0 :
                heapq.heappush(q, i)
       
        res = []
   
        while q :
            node = q.pop()
            res.append(node)

            
            for nei in graph[node]:
                print(in_degree[nei])
                in_degree[nei] -= 1

                if in_degree[nei] == 0 :
                    heapq.heappush(q, nei)
            
        
        for i in range(numCourses):
            if in_degree[i] != 0 :
                return []
        
        return res[::-1]
            
