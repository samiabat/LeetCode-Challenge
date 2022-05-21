class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(amount, count, memo={}):
            if amount in memo:
                return memo[amount]
            if amount == 0:
                return 0
            if amount<0:
                return inf
            arr =  []
            for i in coins:
                arr.append(1+dp(amount-i, count+1, memo))
            memo[amount] = min(arr)
            return memo[amount]
        
        ans = dp(amount, 0)
        if ans ==inf:
            return -1
        return ans