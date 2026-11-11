class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(nums)

        count, res = 1, 1
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i] == sorted_nums[i+1]:
                continue
            if sorted_nums[i] + 1 == sorted_nums[i+1]:
                count += 1
                if count > res:
                    res = count
            else:
                count = 1

        return res