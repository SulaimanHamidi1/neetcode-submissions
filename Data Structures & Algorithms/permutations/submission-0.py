class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        res = []
        seen = [False] * len(nums)

        def backtrack():
            if len(perms) == len(nums):
                res.append(perms[:])
                return
            for i in range(len(nums)):
                if seen[i]:
                    continue
                perms.append(nums[i])
                seen[i] = True
                backtrack()
                seen[i] = False
                perms.pop()
        backtrack()
        return res