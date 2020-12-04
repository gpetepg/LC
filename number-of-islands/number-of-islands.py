class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(row, col):
            grid[row][col] = '-1'
            
            neighbors = [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1)
            ]
            
            for r, c in neighbors:
                if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]) and grid[r][c] == '1':
                    dfs(r, c)
            
            
        island_count = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    island_count += 1
                    dfs(row, col)
                    
        return island_count
       
            
