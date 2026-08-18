class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exist = []
        for num in nums:
            if num in exist:
                return True
            exist.append(num)
        return False