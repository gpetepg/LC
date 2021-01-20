class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(r, c):
            # mark the island
            grid[r][c] = "-1"
            
            neighbors = [
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1)
            ]
            
            for _r, _c in neighbors:
                if _r >= 0 and _c >= 0 and _r < len(grid) and _c < len(grid[r]) and grid[_r][_c] == "1":
                    dfs(_r, _c)
        
        
        
        # number of islands
        number_of_islands = 0
        
        # iterate through the matrix
        for row, rv in enumerate(grid):
            for col, cv in enumerate(rv):
                if grid[row][col] == "1":
                    number_of_islands += 1
                    dfs(row, col)
                
        return number_of_islands
                    
​
