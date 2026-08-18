from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        lst = []
        for num, freq in count.most_common(k):
            lst.append(num)
        return lst
        
        
