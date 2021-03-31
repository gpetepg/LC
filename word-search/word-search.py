class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # dfs on each cell, for each search remember visited cells, and remove cur visited cell right before you return from dfs;
        
        def dfs(board, row, col, word):
            
            if len(word) == 0:
                return True
            
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or board[row][col] != word[0]:
                return False
            
            temp = board[row][col]
            board[row][col] = " "
            
            found = dfs(board, row + 1, col, word[1:]) or dfs(board, row - 1, col, word[1:]) or dfs(board, row, col + 1, word[1:]) or dfs(board, row, col - 1, word[1:])
            
            board[row][col] = temp
            return found
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(board, row, col, word):
                    return True
        return False
                    