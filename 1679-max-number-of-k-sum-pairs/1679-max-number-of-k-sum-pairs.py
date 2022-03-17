class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums)-1
        nums = sorted(nums)
        if len(nums)>=2 and nums[-1]+nums[-2]<k:
            return 0
        count = 0
        while l<r:
            t = nums[l]+nums[r]
            if t==k:
                count+=1
                l+=1
                r-=1
            elif t<k:
                l+=1
            else:
                r-=1
        return count
        