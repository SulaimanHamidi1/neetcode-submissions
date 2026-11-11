class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for digit in digits:
            s += str(digit)
        
        num = int(s)
        num += 1

        res = []
        while num != 0:
            res.append(num % 10)
            num //= 10
        
        return res[::-1]