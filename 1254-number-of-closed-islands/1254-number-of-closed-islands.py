class Solution:
    def isIsland(self, arr, m, n):
        for a, b in arr:
            if 0<a<m and 0<b<n:
                continue
            else:
                return False
        return True
    def closedIsland(self, grid: List[List[int]]) -> int:
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = [[False]*(len(grid[0])) for _ in range(len(grid))]
        def dfs(row, col):
            if 0<=row<len(grid) and 0<=col<len(grid[0]) and grid[row][col]==0 and not visited[row][col]:
                visited[row][col] = True
                arr.append([row, col])
                for i, j in direction:
                    dfs(row+i, col+j)
        count = 0           
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j]:
                    arr = []
                    dfs(i, j)
                    if arr and self.isIsland(arr, len(grid)-1, len(grid[0])-1):
                        count+=1
        return count