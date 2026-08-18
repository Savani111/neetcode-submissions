class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        left = []
        

        i = 0
        while i < len(nums):
            left.append(prefix)
            prefix *= nums[i]
            i += 1
        postfix = 1
        
        j = len(nums) - 1
        while j >= 0:
            left[j] *= postfix
            postfix *= nums[j]
            j -= 1

        return left