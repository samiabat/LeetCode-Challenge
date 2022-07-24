class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dic = {stones[i]:i for i in range(len(stones))}
        @lru_cache(maxsize=None)
        def dp(val, k):
            if k<=0:
                return False
            if val>stones[-1]:
                return False
            if val == stones[-1]:
                return True
            if val not in dic:
                return False
            if k == 1 and val == stones[0]:
                return dp(val+k, k)
            return dp(val+k, k) or dp(val+k+1, k+1) or dp(val+k-1, k-1)
        return dp(stones[0], 1)