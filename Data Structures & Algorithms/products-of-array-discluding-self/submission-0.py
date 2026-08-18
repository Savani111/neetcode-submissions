class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            mult = 1
            for j in range (len(nums)):
                if (j != i) :
                    mult = mult * nums[j]
                
            output.append(mult)
        return output
