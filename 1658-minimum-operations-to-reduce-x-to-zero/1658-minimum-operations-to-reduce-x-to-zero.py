class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left, right, ans, loc = 0, sum(nums), inf, Counter()
        loc[0] = -1
        for i in range(len(nums)):
            left += nums[i]
            loc[left] = i
            right -= nums[i]
            if x - right in loc:
                ans = min(ans, len(nums) - i + loc[x - right])
        return ans if ans != inf else -1
                
            
            
        