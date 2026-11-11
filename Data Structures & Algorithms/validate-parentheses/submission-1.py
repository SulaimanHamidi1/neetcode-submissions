class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {']':'[', ')':'(', '}':'{'}
        res = []

        for c in s:
            if len(res) == 0 and c in my_dict:
                return False
            if c in my_dict:
                if c == ')' and res[-1] == my_dict[')']:
                    res.pop()
                elif c == ']' and res[-1] == my_dict[']']:
                    res.pop()
                elif c == '}' and res[-1] == my_dict['}']:
                    res.pop()
                else:
                    return False
            else:
                res.append(c)

        return len(res) == 0