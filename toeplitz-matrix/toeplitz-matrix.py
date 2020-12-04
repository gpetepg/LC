class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for row, v in enumerate(matrix):
            for col, _v  in enumerate(v):
                if (row == 0 or col == 0 or matrix[row][col] == matrix[row - 1][col - 1]) == False:
                    return False
        return True
        
