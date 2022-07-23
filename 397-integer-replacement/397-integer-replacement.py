class Solution:
    def integerReplacement(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def dp(num):
            if num == 1:
                return 0
            if not num%2:
                return 1+dp(num/2)
            return min(1+dp(num-1), 1+dp(num+1))
        return dp(n)