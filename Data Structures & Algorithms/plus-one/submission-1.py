class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        remainder = 0

        if digits[-1] + 1 > 9:
            res.append(0)
            remainder = 1
        else:
            res.append(digits[-1] + 1)
        for i in range(len(digits) - 2, -1, -1):
            digit = digits[i] + remainder
            if digit > 9:
                res.append(0)
            else:
                res.append(digit)
                remainder = 0
        
        if remainder != 0:
            res.append(1)
        
        return res[::-1]

