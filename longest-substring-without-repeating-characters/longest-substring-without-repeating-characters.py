class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d, res, start = {}, 0, 0
        
        for i, ch in enumerate(s):
            if ch in d:
                start = max(start, d[ch]+1)
            res = max(res, i-start+1)                
            d[ch] = i
            
        return res
