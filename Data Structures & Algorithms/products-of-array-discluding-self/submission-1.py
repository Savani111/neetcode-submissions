class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = []
        left = []
        mult = 1
        for i in range(len(nums)):
            r = 1
            l = 1
            j = 0
            while (j < i):
                r = r * nums[j]
                j += 1
            right.append(r)
            j = i + 1
            while (j < len(nums)):
                l = l * nums[j]
                j += 1
            left.append(l)
        output = []
        for i in range(len(right)):
            output.append((right[i] * left[i]))
        
        return output

