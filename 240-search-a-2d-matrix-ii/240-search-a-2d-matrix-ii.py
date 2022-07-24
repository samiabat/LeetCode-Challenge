class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rightm, rightn = len(matrix)-1, len(matrix[0])-1
        dic = {}
        def dp(r, c, row, col):
            key = (r,c,row, col)
            if key in dic:
                return dic[key]
            midr, midc = (row+r)//2, (col+c)//2
            cur = matrix[midr][midc]
            if cur == target:
                return True
            if r>row or c > col:
                return False
            if target>cur:
                dic[key] = (dp(midr+1, c, row, col) or 
                        dp(r, midc+1, row, col))
                return dic[key]
            dic[key] = (dp(r, c, midr-1, col) or 
                    dp(r, c, row, midc-1))
            return dic[key]
        return dp(0, 0, len(matrix)-1, len(matrix[0])-1)