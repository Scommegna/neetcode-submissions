class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        aux_dict = {}

        for num in nums:
            if num in aux_dict:
                return True
            
            aux_dict[num] = num
        
        return False