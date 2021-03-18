class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        if nums[-1] != len(nums):
            return len(nums)
        
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0
        
        for i in range(1, len(nums)):
            expected = nums[i-1] + 1
            if nums[i] != expected:
                return expected

        