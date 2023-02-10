class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = len(nums1)+len(nums2)
        if a%2==0:
            median =[ a//2-1,a//2]
        else:
            median = [a//2]
        elem = max(median)
        prev = None
        curr=None
        for i in range(elem+1):
            prev = curr
            if len(nums1)==0:
                curr = nums2.pop(0)
            elif len(nums2)==0:
                curr = nums1.pop(0)
            elif nums1[0]<nums2[0]:
                curr = nums1.pop(0)
            else:
                curr = nums2.pop(0)
            print(prev,curr)
        if len(median)==1:
            return curr
        else:
            return (prev+curr)/2