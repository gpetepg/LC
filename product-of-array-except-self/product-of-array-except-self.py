class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        suf, pre = 1, 1
        
        for i in range(len(nums)):
            output.append(pre)
            pre = pre * nums[i]
            
        for i in range(len(nums) -1, -1, -1):
            output[i] = output[i] * suf
            suf = suf * nums[i]
            
        return output