class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = [[1, 1] for i in range(len(nums))]
        ans = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i][0] = max(dp[i][0], 1 + dp[j][1])
                if nums[i] < nums[j]:
                    dp[i][1] = max(dp[i][1], 1 + dp[j][0])
            ans = max(ans, max(dp[i]))
        return ans