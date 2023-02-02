class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        cur = 1
        ans = len(nums) * (len(nums) + 1) // 2
        
        while right < len(nums):
            cur *= nums[right]
            while left<=right and cur >= k:
                ans -= (len(nums) - right)
                cur //= nums[left]
                left += 1
            right += 1
        return ans