class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums[0], nums[-1]); cur = 1; other = 1
        for i in range(len(nums)):
            cur *= nums[i]
            other *= nums[len(nums) - i - 1]
            ans = max(ans, cur, other)
            if cur == 0: cur = 1
            if other == 0: other = 1
        return ans