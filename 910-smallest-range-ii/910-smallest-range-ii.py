class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = nums[0]+k
        right = nums[-1]-k
        ans = nums[-1]-nums[0]
        for i in range(len(nums)-1):
            l = min(nums[i+1]-k, left)
            r = max(nums[i]+k, right)
            ans = min(ans, r-l)
        return ans
        
        
        
        