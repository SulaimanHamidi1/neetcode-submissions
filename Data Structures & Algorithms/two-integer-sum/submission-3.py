class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i, num in enumerate(nums):
            if (target - num) in my_dict and i != my_dict.get(target - num):
                return [my_dict.get(target-num), i]
            my_dict[num] = i
        
        return []
            