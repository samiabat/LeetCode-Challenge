class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        left, right, loc, ans = 0, sum(nums), Counter(), inf
        for i in range(len(nums)):
            left += nums[i]
            right -= nums[i]
            loc[left % p] = i
            if not left % p: loc[p] = i
            if i < len(nums)-1 and right % p == 0: ans = min(ans, i+1)
            if p - right % p in loc: ans = min(ans, i - loc[p - right % p])
        return ans if ans != inf else -1
            