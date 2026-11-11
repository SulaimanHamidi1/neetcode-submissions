class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        prefix[0] = 1
        postfix[-1] = 1

        prod1 = 1
        prod2 = 1

        res = []

        for i in range(1, len(nums)):
            prod1 *= nums[i - 1]
            prefix[i] = prod1
        
        for i in range(len(nums) - 2, -1, -1):
            prod2 *= nums[i + 1]
            postfix[i] = prod2

        for i in range(0, len(nums)):
            res.append(prefix[i] * postfix[i])

        return res



        