class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}

        for s in strs:
            lst = [0] * 26
            for c in s:
                lst[ord(c) - ord('a')] += 1
            
            lst_tup = tuple(lst)
            if lst_tup in freq:
                freq[lst_tup].append(s)
            else:
                freq[lst_tup] = [s]
        
        return list(freq.values())
