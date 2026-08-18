class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}

        for i in range(len(nums)):
            if nums[i] in vals:
                sum = [vals[nums[i]], i]
                return sum
            else:
                val = target - nums[i]
                vals[val] = i