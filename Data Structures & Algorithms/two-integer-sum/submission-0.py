class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aux_dict = {}

        for i, num in enumerate(nums):
            key = target - num
            if key in aux_dict:
                return [aux_dict[key], i]
            else:
                aux_dict[num] = i