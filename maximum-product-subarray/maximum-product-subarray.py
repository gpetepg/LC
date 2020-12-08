class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr = nums[0]
        maxm = nums[0]
        minm = nums[0]
        ans  = nums[0]
        
        for i in nums[1:]:
            curr *= i
            tmp = maxm
            maxm = max(curr, i*maxm, i*minm, i)
            minm = min(curr, i*minm, i*tmp, i)
            curr = max(curr, i)
            ans = max(ans, maxm)
        
        return ans
    
    
    
#         i = 0
#         currentMax, currentMin, ans = nums[0], nums[0], nums[0]
#         for i in range(1, len(nums)):
#             n = nums[i]
#             tmp = currentMax
#             currentMax = max(n, n*currentMax, n*currentMin)
#             currentMin = min(n, n*tmp, n*currentMin)
#             ans = max(ans, currentMax)
#         return ans
