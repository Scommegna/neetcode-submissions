class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        aux_dict = {}
        res = []

        for num in nums:
            if not num in aux_dict:
                aux_dict[num] = 1
            else:
                aux_dict[num] += 1

        for key, value in aux_dict.items():
            tup = (-value, key)

            heapq.heappush(heap, tup)

        for i in range(k):
            _, key = heapq.heappop(heap)
            res.append(key)

        return res


                