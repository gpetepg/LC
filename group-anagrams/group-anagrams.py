class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for i in strs:
            word = "".join(sorted(i))
            res[word] = res.get(word, [])
            res[word].append(i)
            
        return res.values()
