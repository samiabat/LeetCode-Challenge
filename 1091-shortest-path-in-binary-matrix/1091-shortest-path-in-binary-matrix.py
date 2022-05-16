class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direction = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        visit = [[False]*len(grid[0]) for _ in range(len(grid))]
        m = len(grid)
        n = len(grid[0])
        if grid[0][0]:
            return -1
        q = deque([[0, 0]])
        count = 0
        while q:
            size = len(q)
            count+=1
            for _ in range(size):
                row, col = q.popleft()
                if visit[row][col]:
                    continue
                visit[row][col] = True
                if (row, col)==(m-1, n-1):
                    return count
                for i, j in direction:
                    r, c = row+i, col+j
                    if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c]==0 and not visit[r][c]:
                        q.append([r,c])
        return -1
                
                