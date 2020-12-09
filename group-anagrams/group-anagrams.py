class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for w in strs:
            word = "".join(sorted(w))
            res[word] = res.get(word, [])
            res[word].append(w)
            
        return res.values()
