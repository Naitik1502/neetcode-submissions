class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n_rows = len(grid)
        n_cols = len(grid[0])

        def dfs(row_val, col_val):
            nonlocal grid
            nonlocal n_rows
            nonlocal n_cols

            if not ((-1 < row_val < n_rows) and (- 1 < col_val < n_cols)) :
                return 
            
            print("started dfs")
            print(row_val)
            print(col_val)
            print(grid[row_val][col_val])
            if grid[row_val][col_val] == "1" :
                grid[row_val][col_val] = "0"
            
                dfs(row_val - 1, col_val)
                dfs(row_val + 1, col_val)
                dfs(row_val, col_val - 1)
                dfs(row_val, col_val + 1)
        
        cnt = 0
        
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == "1" :
                    cnt += 1 
                    dfs(i, j)
                    print(grid)
        
        return cnt



           
