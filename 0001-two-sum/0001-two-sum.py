class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        for i in range(len(nums)):
            remaining = target - nums[i]

            if remaining in nums[i + 1:]:
                j = nums.index(remaining, i + 1)
                return [i, j]

        return result