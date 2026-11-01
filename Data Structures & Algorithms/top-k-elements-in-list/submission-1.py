class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        aux_dict = {}

        aux_arr = []

        for num in nums:
            if not num in aux_dict:
                aux_dict[num] = 1
            else:
                aux_dict[num] += 1


        lowest_key = -1
        lowest_value = -1

        for key, value in aux_dict.items():
            length = len(aux_arr)    

            if length != 0:
                if length < k:
                    aux_arr.append(key)

                    if value < lowest_value:
                        lowest_key = key
                        lowest_value = value
                else:
                    if value > lowest_value:
                        aux_arr.remove(lowest_key)
                        aux_arr.append(key)
                        lowest_value = value
                        lowest_key = key

                        for num in aux_arr:
                            if aux_dict[num] <= lowest_value:
                                lowest_key = num
                                lowest_value = aux_dict[num]
            else:
                aux_arr.append(key)
                lowest_key = key
                lowest_value = value

        return aux_arr


                