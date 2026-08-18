class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        vals = {}
        for i in range(len(numbers)):
            vals[numbers[i]] = i
        for i in range(len(numbers)):
            if (target - numbers[i]) in vals:
                return [i + 1, vals[target - numbers[i]] + 1]