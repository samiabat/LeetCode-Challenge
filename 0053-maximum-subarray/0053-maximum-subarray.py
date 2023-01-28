class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur, best = 0, -inf
        for num in nums:
            cur = max(num, cur + num)
            best = max(cur, best)
        return best