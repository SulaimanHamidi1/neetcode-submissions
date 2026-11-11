class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(reamining, start):
            if reamining == 0:
                res.append(path[:])
            elif reamining < 0:
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(reamining - nums[i], i)
                path.pop()
    
        backtrack(target, 0)
        return res