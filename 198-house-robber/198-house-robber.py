class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(index = 0, tot = 0, memo = {}):
            if index>=len(nums):
                return tot
            else:
                if index in memo:
                    return memo[index]
                else:
                    cur = nums[index]
                    ans2 = 0
                    ans1 =  cur + max(dp(index+2), dp(index+3))
                    if index<len(nums)-1:
                        ans2 = nums[index + 1] + max(dp(index+3), dp(index+4))
                    memo[index] = max(ans1, ans2)
            return memo[index]
        return dp()
        