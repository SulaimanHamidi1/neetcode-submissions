class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1;
            
            key = str(count)
            my_dict.setdefault(key, []).append(s)
        
        return list(my_dict.values())