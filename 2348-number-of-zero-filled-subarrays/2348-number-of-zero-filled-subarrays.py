class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans =   len(nums)  * (len(nums) + 1) // 2
        
        left, right = -1, 0
        
        for right in range(len(nums)):
            if nums[right]:
                ans -= (right - left)*(len(nums) - right)
                left = right
        return ans