class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def dp(index):
            if index<len(nums)-1 and nums[index]==0:
                return False
            if index>=len(nums)-1:
                return True
            for i in range(nums[index], 0, -1):
                if dp(index+i):
                    return True
            return False
        return dp(0)