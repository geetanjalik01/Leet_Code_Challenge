from functools import lru_cache

class Solution:
    def minDays(self, n: int) -> int:

        @lru_cache(None)
        def dfs(x):
            if x <= 1:
                return x
            option1 = (x % 2) + dfs(x // 2)
            option2 = (x % 3) + dfs(x // 3)
            return 1 + min(option1, option2)

        return dfs(n)