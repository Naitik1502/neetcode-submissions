class Solution:
    def solve(self, board: List[List[str]]) -> None:

        x_sample = []
        

        n_rows = len(board)
        n_cols = len(board[0])

        for i in range(n_rows):
            row = []
            for j in range(n_cols):
                row.append(board[i][j])
                
                board[i][j] = "X"
            x_sample.append(row)
        
        

        visited = set()
        
        def dfs(row, col):
            if (not ((-1 < row < n_rows) and (-1< col < n_cols))) or x_sample[row][col] == 'X' or (row , col) in visited:
                return 
          
            board[row][col] = 'O'
            visited.add((row,col))

            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                dfs(row +dr, col +dc)
        
        for i in range(n_cols):
            if x_sample[0][i] == "O" :
                dfs(0,i)
            if x_sample[n_rows-1][i] == "O" :
          
                dfs(n_rows-1,i)
        
        for i in range(n_rows):
            if x_sample[i][0] == "O" :
                dfs(i,0)
            if x_sample[i][n_cols-1] == "O" :
                dfs(i,n_cols-1)
        

        
            
            
