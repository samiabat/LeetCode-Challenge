class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        memo = {}
        def dp(index, cur = set()):
            if index in memo:
                return memo[index]
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