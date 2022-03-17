class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        if len(nums)==1:
            return 0
        while left<=right:
            mid = (right+left)//2
            if mid==0 and nums[mid]>nums[mid+1]:
                return mid
            elif mid==len(nums)-1 and nums[mid]>nums[mid-1]:
                return mid
            elif mid>0 and mid<len(nums)-1 and nums[mid]>nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid+1]>nums[mid]:
                left = mid+1
            else:
                right = mid-1
            