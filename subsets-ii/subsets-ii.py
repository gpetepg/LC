class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        output = []
        def backtrack(first = 0, cur = []):
            output.append(cur[:])
            for i in range(first, n):
				#in case same combination is used many times
                if i>first and nums[i] == nums[i-1]:
                    continue
                else:
                    cur.append(nums[i])
                    backtrack(i+1, cur)
                    cur.pop()
        backtrack()
        return output
