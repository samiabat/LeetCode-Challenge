class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        
        left = nums[0]
        for i in range(1, len(nums)):
            left = min(nums[i-1], left)
            if nums[i] > left: ans = max(ans, nums[i]-left)
        return ans