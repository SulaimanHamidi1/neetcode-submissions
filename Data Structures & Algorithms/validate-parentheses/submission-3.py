class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {']':'[', ')':'(', '}':'{'}
        res = []

        for c in s:
            if c in my_dict:
                if res and res[-1] == my_dict[c]:
                    res.pop()
                else:
                    return False
            else:
                res.append(c)

        return len(res) == 0