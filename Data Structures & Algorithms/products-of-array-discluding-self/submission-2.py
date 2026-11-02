class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums

        mult = 1
        pre, pos, result = [], [], []

        for num in nums:
            mult *= num
            pre.append(mult)

        mult = 1

        for i in range(len(nums) - 1, -1, -1):
            mult *= nums[i]
            pos.append(mult)

        pos.reverse()

        for i in range(len(nums)):
            if i == 0:
                result.append(pos[i + 1])
            elif i == len(nums) - 1:
                result.append(pre[i - 1])
            else:
                result.append(pre[i - 1] * pos[i + 1])
  

        return result
