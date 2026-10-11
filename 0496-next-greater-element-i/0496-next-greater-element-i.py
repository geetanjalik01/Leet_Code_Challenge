
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for num in nums1:
            result = -1
            found = False

            for n in nums2:
                if n == num:
                    found = True
                    continue

                if found and n > num:
                    result = n
                    break

            ans.append(result)

        return ans
