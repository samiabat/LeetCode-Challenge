class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        loc = {0:-1}
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            cur %= k
            if cur % k in loc and loc[cur % k] != i-1: return True
            if cur not in loc: loc[cur] = i
        return False
            