class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(maxsize = None)
        def rec(index):
            if index>=len(cost):
                return 0
            cur = cost[index]
            return min(cur + rec(index + 1), cur + rec(index+2))
        return min(rec(0), rec(1))