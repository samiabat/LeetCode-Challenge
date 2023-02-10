class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num.sort()
        if not len(num)%2:
            return (num[len(num)//2 -1] + num[len(num)//2])/2
        return num[len(num)//2]
            