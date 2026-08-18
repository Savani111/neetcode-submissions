class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        val = 0
        lar = 1
        found = set()
        count = 1
        for num in nums:
            found.add(num)
        for curr in found:
            if (curr - 1) not in found:
                val = curr
                count = 1
                while (val + 1 in found):
                    count+=1
                    val +=1
                lar = max(lar, count)
                    
            else:
                continue
            
            
        return lar