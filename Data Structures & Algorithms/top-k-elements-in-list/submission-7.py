class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}

        for num in nums:
            if num not in data:
                data[num] = 0
            data[num] += 1
        sort = dict(sorted(data.items(), key=lambda item: item[1], reverse = True))
        lst = []
        for i in range(k):
                lst.append(list(sort.keys())[i])

        return lst