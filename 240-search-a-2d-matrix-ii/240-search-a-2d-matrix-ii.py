class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rightm, rightn = len(matrix)-1, len(matrix[0])-1
        @lru_cache(maxsize=None)
        def dp(r, c, row, col):
            midr, midc = (row+r)//2, (col+c)//2
            cur = matrix[midr][midc]
            if cur == target:
                return True
            if r>row or c > col:
                return False
            if target>cur:
                return (dp(midr+1, c, row, col) or 
                       dp(midr+1, midc+1, row, col) or 
                        dp(r, midc+1, row, col))
            else:
                return (dp(r, c, midr-1, col) or 
                      dp(r, c, midr-1, midc-1) or 
                        dp(r, c, row, midc-1))
        return dp(0, 0, len(matrix)-1, len(matrix[0])-1)