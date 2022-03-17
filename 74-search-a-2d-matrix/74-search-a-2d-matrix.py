class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        fin = []
        for i in matrix:
            if target<=i[-1]:
                fin = i
                break
        if not fin:
            return False
        left = 0
        right = len(fin)-1
        while left<=right:
            mid = (left+right)//2
            if fin[mid]<target:
                left = mid+1
            elif fin[mid]>target:
                right = mid-1
            else:
                return True
        return False