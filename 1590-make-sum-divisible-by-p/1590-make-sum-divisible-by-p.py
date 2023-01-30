class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        left, right, loc, ans = 0, sum(nums), Counter(), len(nums)
        for i in range(len(nums)):
            left += nums[i]
            right -= nums[i]
            loc[left % p] = i
            
            if not left % p:
                ans = min(ans, len(nums) - i - 1)
                
            if not right % p:
                ans = min(ans, i+1)
                
            if p - right % p in loc:
                ans = min(ans, i - loc[p - right % p])
                
        return ans if ans < len(nums) else -1
            