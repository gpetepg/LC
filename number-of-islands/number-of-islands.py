class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(r, c):
            grid[r][c] = "HAHAHAH"
            
            neighbors = [
                (r-1, c),
                (r+1, c),
                (r, c-1),
                (r, c+1)
            ]
            
            for _r, _c in neighbors:
                if _r >= 0 and _c >= 0 and _r < len(grid) and _c < len(grid[r]) and grid[_r][_c] == "1":
                    dfs(_r, _c)
            
        number_of_islands = 0
            
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    number_of_islands += 1
                    dfs(row, col)
                    
        return number_of_islands
                    
