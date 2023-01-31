class Solution:
    def maxProfit(self, prices: List[int]) -> int:  
        dp, ans = [0] * (len(prices)), 0        
        for idx in range(1, len(prices)):
            for idx2 in range(idx):
                if idx2>=2:
                    dp[idx] = max(dp[idx-1],dp[idx], max(0, prices[idx] - prices[idx2]) + dp[idx2 - 2])
                else:
                    dp[idx] = max(dp[idx-1],dp[idx], max(0, prices[idx] - prices[idx2]))
            ans = max(ans, dp[idx])
        return ans
        
        
            
            
            
        