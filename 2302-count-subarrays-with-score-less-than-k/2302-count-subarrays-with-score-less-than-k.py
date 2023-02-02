class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = right = cur = size = 0
        ans = len(nums) * (len(nums) + 1) // 2
        
        while right < len(nums):
            cur += nums[right]
            size += 1
            
            while left <= right and cur * size >= k:
                ans -= (len(nums) - right)
                cur -= nums[left]
                size -= 1
                left += 1
            right += 1
        return ans