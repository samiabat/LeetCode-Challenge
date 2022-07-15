class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def dp(index, memo = {}):
            if index in memo:
                return memo[index]
            if index>=len(nums)-1:
                return True
            if nums[index]==0:
                return False
            for i in range(nums[index], 0, -1):
                if dp(index+i):
                    memo[index] = True
                    return memo[index]
            memo[index] = False
            return memo[index]
        return dp(0)