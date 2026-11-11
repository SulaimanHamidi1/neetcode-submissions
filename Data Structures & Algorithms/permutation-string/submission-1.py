class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False
        
        s1_arr = [0] * 26
        s2_arr = [0] * 26
        for c in s1:
            s1_arr[ord(c) - ord('a')] += 1
        
        length = len(s1)
        l = 0
        for r in range(len(s2)):
            s2_arr[ord(s2[r]) - ord('a')] += 1

            if r - l + 1 > length:
                s2_arr[ord(s2[l]) - ord('a')] -= 1
                l += 1
                
            if s1_arr == s2_arr:
                return True
            
        return False

        
