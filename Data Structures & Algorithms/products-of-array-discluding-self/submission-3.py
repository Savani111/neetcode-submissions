class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []

        l = 1
        for num in nums:
            left.append(l)
            l = l * num
        
        
        r = 1
        for i in reversed(range(len(nums))):
            left[i] *= r 
            r = r * nums[i]
        

        

        return left
        
