class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def dp(step):
            if step == n:
                return 1
            if step > n:
                return 0
            return dp(step+1) + dp(step+2)
        return dp(0)