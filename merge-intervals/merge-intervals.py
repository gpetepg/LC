class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        merged = []
    
        for i in intervals:
            if not merged or i[0] > merged[-1][1]:
                merged.append(i)
            else:
                merged[-1][1] = max(merged[-1][1], i[1])
        return merged