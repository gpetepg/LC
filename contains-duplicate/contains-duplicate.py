class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = {}
        
        for i in nums:
            res[i] = res.get(i, 0) + 1
        
        if sum(res.values()) == len(res.values()):
            return False
        
        return True
        
