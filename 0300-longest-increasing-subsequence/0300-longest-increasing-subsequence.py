class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] <= nums[j]: continue
                dp[i] = max(dp[i], dp[j])
            dp[i] += 1
        return max(dp.values())
        
        