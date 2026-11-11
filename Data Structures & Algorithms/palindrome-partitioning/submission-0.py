class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palinds = []
        res = []
        
        def isPalindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(start):
            if start == len(s):
                res.append(palinds[:])
                return
            for i in range(start, len(s)):
                if isPalindrome(s[start:i+1]):
                    palinds.append(s[start:i+1])
                    backtrack(i + 1)
                    palinds.pop()
                

        backtrack(0)
        return res

        