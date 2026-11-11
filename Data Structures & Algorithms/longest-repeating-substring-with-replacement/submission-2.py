class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        """
            Intuition:
            1) We need our current window length: (r - l + 1)
            2) We get the character that appears the most in that window: (max_freq)
            3) window_length - max_freq is the number of all other characters in our window
                Example: AAABABB, if our window is from 0:4 then 5 - 4 = 1.
            4) Since we can only replace up to k characters,
                we move our left pointer to ensure the window size stays correct.
        """
        freq = {}
        longest = l = 0
        max_freq = 0

        for r in range(len(s)):
            c = s[r]
            freq[c] = 1 + freq.get(c, 0)
            max_freq = max(max_freq, freq[c])

            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        
        return longest
            


