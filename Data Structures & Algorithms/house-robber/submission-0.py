class Solution:
    def rob(self, nums: List[int]) -> int:
        """ top down """

        memo = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i+1), dfs(i+2) + nums[i])
            return memo[i]
        
        return dfs(0)