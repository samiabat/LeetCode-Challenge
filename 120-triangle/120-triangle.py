class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        col = 0
        row = 0
        def dp(row = 0, col = 0, tot = 0, memo = {}):
            if row == len(triangle):
                return tot
            cur = triangle[row][col]
            if (row, col) in memo:
                return memo[(row, col)]
            else:
                memo[(row, col)] = cur + min(dp(row+1, col), dp(row+1, col+1))
            return memo[(row,col)]
        return dp()