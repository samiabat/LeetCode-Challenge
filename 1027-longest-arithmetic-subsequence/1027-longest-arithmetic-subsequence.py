class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        large = max(nums)
        small = min(nums)
        
        dp = [{i:1 for i in range(small-large, large+large+1)} for _ in range(len(nums))]
        ans = 0
        mp = {}
        
        for i in range(len(nums)-1, -1, -1):
            for key in dp[i]:
                if nums[i] + key in mp:
                    dp[i][key] = max(dp[i][key], 1 + dp[mp[nums[i] + key]][key])
                    ans = max(ans, dp[i][key])
            mp[nums[i]] = i
        return ans