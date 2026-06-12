class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        #Time Complexity :- 
        
        graph = defaultdict(list)

        for e in edges :
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        
        visited = [0]*n
        
        def dfs(node):

            if len(graph[node]) == 0 or visited[node] == 1:
                visited[node] = 1
                return 
            
            visited[node] = 1

            for nei in graph[node]:
                dfs(nei)
        
        cnt = 0
        
        for i in range(n):
            if visited[i] == 1 :
                continue
            cnt += 1
            dfs(i)
        
        return cnt


            
