class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            visit.append([False]*n)
        val = 0
        def dfs(grid, visit, r, c):
            if r>=0 and c>=0 and r< len(grid) and c<len(grid[0]):
                if not visit[r][c] and grid[r][c]==1:
                    visit[r][c]=True
                    arr.extend([1])
                    dfs(grid, visit, r+1, c)
                    dfs(grid, visit, r-1, c)
                    dfs(grid, visit, r, c+1)
                    dfs(grid, visit, r, c-1)                       
        for i in range(m):
            for j in range(n):
                arr = []
                if not visit[i][j]:
                    dfs(grid, visit, i, j)
                    if sum(arr)>val:
                        val = sum(arr)
        return val