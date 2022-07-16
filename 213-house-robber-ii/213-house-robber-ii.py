class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dp(index, flag = 0):
            if index>=len(nums):
                return 0
            notchose = dp(index+1, flag)
            if flag and index == len(nums)-1:
                return notchose
            if index==0:
                chose = nums[index]+dp(index+2, flag = 1)
            else:
                chose = nums[index]+dp(index+2, flag)
            return max(chose, notchose)
        return dp(0)