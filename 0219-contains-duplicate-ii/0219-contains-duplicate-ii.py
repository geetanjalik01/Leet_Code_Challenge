class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos = {}

        for i, x in enumerate(nums):
            if x in pos:
                if i - pos[x] <= k:
                    return True
            pos[x] = i

        return False