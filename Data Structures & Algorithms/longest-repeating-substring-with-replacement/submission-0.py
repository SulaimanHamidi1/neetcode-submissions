class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = dict.fromkeys(s, 0)
        res = 0

        for c in hashmap:
            l = 0
            for r in range(len(s)):
                if s[r] == c:
                    hashmap[s[r]] += 1
                while (r - l + 1) - hashmap[c] > k:
                    if s[l] == c:
                        hashmap[s[l]] -= 1
                    l += 1
                res = max(res, r - l + 1)
        return res
                

