class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        def dp(index, cur = set(), memo = {}):
            if index in memo:
                return memo[index]
            if index>=len(nums):
                return 0
            current = nums[index]
            if current in cur:
                return 0
            cur.add(current)
            memo[index] = 1 + dp(current, cur)
            return memo[index]
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, dp(i))
        return ans