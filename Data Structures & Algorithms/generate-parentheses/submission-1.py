class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s, close, open):
            if close > open:
                return
            if len(s) == 2 * n:
                res.append(s)
                return

            if open < n:
                backtrack(s + '(', close, open + 1)
            if close <= open:
                backtrack(s + ')', close + 1, open)


        backtrack("", 0, 0)
        return res