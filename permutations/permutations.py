class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(nums, visited, subset, res):
            if len(subset) == len(nums):
                res.append(subset)
                
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    backtrack(nums, visited, subset + [nums[i]], res)
                    visited.remove(i)
            
            
        visited = set()
        res = []
        backtrack(nums,visited,[],res)
        return res