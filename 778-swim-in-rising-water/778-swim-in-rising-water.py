class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        Q = [[grid[0][0], 0, 0]]
        
        visit = set((0,0))
        time = 0
        
        while Q:
            top = heappop(Q)
            row, col = top[1:]
            time = max(time, grid[row][col])
            if row == len(grid)-1 and col == len(grid)-1:
                return time
            
            possible_moves = [[row+1, col], [row-1, col], [row, col+1],[row,col-1]]
            
            for i, j in possible_moves:
                if 0<=i<len(grid) and 0<=j<len(grid) and (i,j) not in visit:
                    visit.add((i,j))
                    heappush(Q, [grid[i][j], i, j])
        return time        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Q=[[grid[0][0],0,0]]
        # seen=[[False]*len(grid) for _ in range(len(grid))]
        # time=0
        # while Q:
        #     cur=heapq.heappop(Q)
        #     time=max(time,cur[0])
        #     if cur[1]==len(grid)-1 and cur[2]==len(grid)-1:
        #         return time
        #     for i,j in [[cur[1]+1,cur[2]],[cur[1],cur[2]+1],[cur[1]-1,cur[2]],[cur[1],cur[2]-1]]:
        #         if 0<=i<len(grid) and 0<=j<len(grid) and seen[i][j]==False:
        #             heapq.heappush(Q,[grid[i][j],i,j])
        #             seen[i][j]=True
        
        
        
        
        
        
        
        
        
        
        # m = len(grid)
        # n = len(grid[0])
        # uf = [[(i, j) for j in range(n)] for i in range(m)]
        # def find(i, j):
        #     if not (i,j) == uf[i][j]:
        #         uf[i][j] = find(*uf[i][j])
        #     return uf[i][j]
        # order = sorted((grid[i][j], i, j) for j in range(n) for i in range(m))
        # for val, i, j in order:
        #     for ni, nj in [[i+1, j], [i-1,j], [i, j+1], [i, j-1]]:
        #         if (0<=ni<m) and (0<=nj<n) and grid[ni][nj] <= val:
        #             ai, aj = find(i, j)
        #             bi, bj = find(ni, nj)
        #             uf[ai][aj] = uf[bi][bj]
        #     if find(0,0) == find(m-1, n-1):
        #         return val