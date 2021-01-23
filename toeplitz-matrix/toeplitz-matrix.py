class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if (row == 0 or col == 0 or matrix[row][col] == matrix[row - 1][col - 1]) == False:
                    return False
        return True
    
