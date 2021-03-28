class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_substr = 0
        a_pntr, b_pntr = 0, 0
        curr_chrs = set()
        
        while b_pntr < len(s):
    
            if s[b_pntr] not in curr_chrs:
                curr_chrs.add(s[b_pntr])
                b_pntr += 1
                longest_substr = max(longest_substr, len(curr_chrs))
            else:
                curr_chrs.remove(s[a_pntr])
                a_pntr += 1
                
        return longest_substr
                
        
        
        
        
                
                
        