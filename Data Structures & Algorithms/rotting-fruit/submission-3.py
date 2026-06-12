class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        from collections import deque

        r, c = len(grid), len(grid[0])

    
        q = deque(set())

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2 :
                    q.append((i,j))
        
        print(q)
        level = -1

        visited = set()

        if len(q) == 0 :

            for i in range(r):
                for j in range(c):
                    if grid[i][j] == 1 :
                        return -1 
            
            return 0

        
        
        while q :
            level += 1
            len_level = len(q)
            print(q)

            for _ in range(len_level): 
                n_r, n_c = q.popleft()    
                grid[n_r][n_c] = 2   
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    row = n_r + dr
                    col = n_c + dc 

                    if -1< row < r and -1 < col < c and grid[row][col] == 1 :
                        if (row,col) not in visited :
                            q.append((row,col))
                            visited.add((row,col))

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 :
                    return -1   
        
        return level  





        