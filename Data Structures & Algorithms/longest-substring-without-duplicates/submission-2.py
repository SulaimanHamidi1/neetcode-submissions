class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        uniques = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in uniques:
                uniques.remove(s[l])
                l += 1
            uniques.add(s[r])
            longest = max(longest, r - l + 1)

        return longest