class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = " ".join(str(n)).split(" ")
        pro, sm = 1, 0
        
        for i in s:
            pro *= int(i)
            
        for i in s:
            sm += int(i)
            
        return pro - sm