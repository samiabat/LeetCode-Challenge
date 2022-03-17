class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        i = 0
        while l<=r:
            m = (l+r)//2
            if nums[m]<target:
                l = m+1
            elif nums[m]>target:
                r = m-1
            else:
                l = m-1
                r = m+1
                arr = []
                if len(nums)==1:
                    return [0, 0]
                while l>=0 and nums[l]==target:
                    l-=1
                arr.append(l+1)
                while r<=len(nums)-1 and nums[r]==target:
                    r+=1
                arr.append(r-1)
                return arr
        return [-1, -1]
            