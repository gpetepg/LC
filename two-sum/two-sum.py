class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        
        for i, v in enumerate(nums):
            if v in res:
                return([res[v], i])
            res[target - v] = i
            
        return []
