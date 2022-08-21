class Solution:
    def _cleaner(self, string):
        result = []
        for char in string:
            if char == "#":
                if result:
                    result.pop()
            else:
                result.append(char)
        print(result)
        return(result)
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self._cleaner(s) == self._cleaner(t)
        