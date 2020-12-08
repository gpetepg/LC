class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        maxm = nums[0]
        
        for i in nums[1:]:
            curr += i
            maxm = max(curr, maxm, i)
            curr = max(curr, i)
        
        return maxm
