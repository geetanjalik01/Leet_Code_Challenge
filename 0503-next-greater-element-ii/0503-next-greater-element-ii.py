
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(n):
            result = -1

            for j in range(1, n):
                next_index = (i + j) % n

                if nums[next_index] > nums[i]:
                    result = nums[next_index]
                    break

            ans.append(result)

        return ans
