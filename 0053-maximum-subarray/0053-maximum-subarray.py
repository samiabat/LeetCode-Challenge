class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left_min, cur, ans = 0, 0, -inf
        for num in nums:
            cur += num
            ans = max(ans, cur - left_min)
            left_min = min(left_min, cur)
        return ans
            
        