class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        aux = {}

        for string in strs:
            srted = "".join(sorted(string))

            if not srted in aux:
                aux[srted] = [string]
            else:
                aux[srted].append(string)

        for value in aux.values():
            result.append(value)

        return result