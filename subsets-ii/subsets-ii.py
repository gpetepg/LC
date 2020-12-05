class Solution:
    def subsetsWithDup(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        subsets = [[]]
        for num in arr:
            for i in range(len(subsets)):
                curr = subsets[i]
                if curr + [num] not in subsets:
                    subsets.append(curr + [num])
        return subsets
