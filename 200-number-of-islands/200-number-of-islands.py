class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = []
        count = 0
        for i in range(len(grid)):
            visit.append([False]*len(grid[0]))
        def dp(r, c):
            possible_move = [[r+1, c], [r-1, c], [r, c+1], [r,c-1]]
            for i, j in possible_move:
                if 0<=i<len(grid) and 0<=j<len(grid[0]):
                    if grid[i][j]=="1" and not visit[i][j]:
                        visit[i][j] = True
                        dp(i,j)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visit[i][j] and grid[i][j]=="1":
                    count+=1
                    dp(i, j)
        return count