class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(maxsize=None)
        def dp(index, amount):
            if amount==0:
                return 0
            if amount<0:
                return inf
            if index>=len(coins):
                return inf
            chose = 1+dp(index+1, amount-coins[index])
            n_chose = dp(index+1, amount)
            rpt = 1+dp(index, amount-coins[index])
            return min(chose, n_chose, rpt)
        
        ans = dp(0, amount)
        if ans == inf:
            return -1
        return ans