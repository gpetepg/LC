class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        p, s = 1, 1
        
        for i in range(len(nums)):
            output.append(p)
            p = p * nums[i]
            
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * s
            s = s * nums[i]
            
        return output
                      
