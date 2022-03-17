class Solution:
    def finder(self, nums):
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]>nums[-1]:
                left = mid+1
            elif nums[mid]<nums[-1]:
                right = mid-1
            else:
                break
        return left
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.finder(nums)
        if target>nums[-1]:
            left=0
            right=pivot-1
        else:
            left=pivot
            right=len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]>target:
                right = mid-1
            elif nums[mid]<target:
                left = mid+1
            else:
                return mid
        return -1
        