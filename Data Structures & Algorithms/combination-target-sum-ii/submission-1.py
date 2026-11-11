class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        path = []
        res = []
        
        def backtrack(remaining, start):
            if remaining == 0:
                res.append(path[:])
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                backtrack(remaining - candidates[i], i + 1)
                path.pop()
            
        backtrack(target, 0)
        return res