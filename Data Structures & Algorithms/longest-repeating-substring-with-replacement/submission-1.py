class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_dict = {}
        res = l = 0
        max_frq = 0

        for r in range(len(s)):
            my_dict[s[r]] = 1 + my_dict.get(s[r], 0)
            max_frq = max(my_dict[s[r]], max_frq)

            while (r - l + 1) - max_frq > k:
                my_dict[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
            

