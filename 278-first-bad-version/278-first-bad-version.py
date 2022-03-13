# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        while l<=r:
            mid = (l+r)//2
            if isBadVersion(mid+1) and not isBadVersion(mid):
                return mid+1
            elif not isBadVersion(mid):
                l = mid
            else:
                r= mid