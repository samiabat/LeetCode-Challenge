class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mini = 0;maxi = 0;ans = 0;cur = 0
        for num in nums:
            cur += num
            mini = min(mini, cur)
            maxi = max(maxi, cur)
            ans = max(ans, abs(cur - mini), abs(cur-maxi))
        return ans
            
            