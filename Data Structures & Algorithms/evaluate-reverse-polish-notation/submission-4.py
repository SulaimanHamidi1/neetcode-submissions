class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        for token in tokens:
            if token == '+':
                res.append(res.pop() + res.pop())
            elif token == '-':
                a, b = res.pop(), res.pop()
                res.append(b - a)
            elif token == '*':
                res.append(res.pop() * res.pop())
            elif token == '/':
                a, b = res.pop(), res.pop()
                res.append(int(float(b) / a))
            else:
                res.append(int(token))

        return res[0]