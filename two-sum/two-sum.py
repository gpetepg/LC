class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        
        for i, v in enumerate(nums):
            pair = target - v # 9 - 2 = 7
            
            if v in pairs:
                return [pairs[v], i]
            
            pairs[pair] = i
            
        return []
