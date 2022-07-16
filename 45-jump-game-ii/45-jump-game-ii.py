class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = len(nums)-1
        @lru_cache(maxsize=None)
        def dp(index):
            nonlocal ans
            if index>=len(nums)-1:
                return 0
            if index<len(nums)-1 and nums[index]==0:
                return len(nums)-1
            for i in range(1, nums[index]+1):
                ans = min(ans, 1+dp(index+i))
            return ans
        return dp(0)