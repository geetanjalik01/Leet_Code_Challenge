class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0

        while i < len(nums):
            start = i

            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1

            if start == i:
                ans.append(str(nums[start]))
            else:
                ans.append(f"{nums[start]}->{nums[i]}")

            i += 1

        return ans