class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        def dp(row, col, memo = {}):
            
            key = (row, col)
            if key in memo:
                return memo[key]
            if row<0 or col<0:
                return 0
            if row>=m or col>=n:
                return 0
            if obstacleGrid[row][col]==1:
                return 0
            if col == 0 and row == 0:
                return 1
            memo[key] =  dp(row-1, col) + dp(row, col-1)
            return memo[key]
        return dp(m-1, n-1)
            