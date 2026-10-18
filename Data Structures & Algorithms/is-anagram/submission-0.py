class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        aux_dict = {}

        for letter in s:
            if not letter in aux_dict:
                aux_dict[letter] = 1
            else:
                aux_dict[letter] += 1

        for letter in t:
            if not letter in aux_dict:
                return False
            
            aux_dict[letter] -= 1

        for key, value in aux_dict.items():
            if value != 0:
                return False

        return True