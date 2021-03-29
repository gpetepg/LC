class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if len(matrix) == 0:
            return res
        
        r_s = 0
        r_e = len(matrix) - 1
        c_s = 0
        c_e = len(matrix[0]) - 1
        
        
        res = []
        
        while r_s <= r_e and c_s <= c_e:
        
            # right iteration
            for i in range(c_s, c_e + 1):
                res.append(matrix[r_s][i])

            r_s += 1

            # down iteration
            for i in range(r_s, r_e + 1):
                res.append(matrix[i][c_e])
                
            c_e -= 1

            # left iteration
            if (r_s <= r_e):
                for i in range(c_e, c_s-1, -1):
                    res.append(matrix[r_e][i])
                
            r_e -= 1

            # up iteration
            if (c_s <= c_e):
                for i in range(r_e, r_s-1, -1):
                    res.append(matrix[i][c_s])

            c_s += 1
        
        return res
        
        
        