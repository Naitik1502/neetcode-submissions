class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        from collections import deque

        c_map = defaultdict(int)
        graph = defaultdict(list)


        for c in prerequisites :
            a = c[0]
            b = c[1]
            c_map[b] += 1
            graph[a].append(b)
        
        q = deque()

        res = []

        for i in range(numCourses):
            in_degree = c_map[i]
            if in_degree == 0 :
                q.append(i)
            
        while q :
            node = q.popleft()
            res.append(node)

            for nei in graph[node]:
                c_map[nei] -= 1
                if c_map[nei] == 0 :
                    q.append(nei)
        
        return (len(res) == numCourses)




        