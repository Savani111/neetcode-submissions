class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}

        for num in nums:
            data[num] = data.get(num, 0) + 1
            
        sort = dict(sorted(data.items(), key=lambda item: item[1], reverse = True))
        val = list(sort.keys())
        lst = []
        for i in range(k):
                lst.append(val[i])

        return lst