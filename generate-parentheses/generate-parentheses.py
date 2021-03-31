class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(output_arr, curr_string, opn, close, _max):
            if len(curr_string) == n * 2:
                output_arr.append(curr_string)
                return

            if opn < _max:
                backtrack(output_arr, curr_string + "(", opn + 1, close, _max)
            if close < opn:
                backtrack(output_arr, curr_string + ")", opn, close + 1, _max)
        
        res = []
        backtrack(res, "", 0, 0, n)
        return res