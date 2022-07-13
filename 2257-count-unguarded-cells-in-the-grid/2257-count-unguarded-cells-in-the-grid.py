class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def moveLeft(r, c):
            r, c = r, c-1
            if c<0 or grid[r][c] == "W" or grid[r][c] =="G":
                return
            grid[r][c]=True
            moveLeft(r, c)
        def moveRight(r, c):
            r, c = r, c+1
            if c>=n or grid[r][c] == "W" or grid[r][c] =="G":
                return
            grid[r][c]=True
            moveRight(r, c)
        def moveTop(r, c):
            r, c = r-1, c
            if r<0 or grid[r][c] == "W" or grid[r][c] =="G":
                return
            grid[r][c]=True
            moveTop(r, c)
        def moveBot(r, c):
            r, c = r+1, c
            if r>=m or grid[r][c] == "W" or grid[r][c] =="G":
                return
            grid[r][c]=True
            moveBot(r,c)
        grid = []
        
        
        for i in range(m):
            grid.append([False]*n)
        for r, c in guards:
            grid[r][c] = "G"
        for r, c in walls:
            grid[r][c] = "W"
        for r, c in guards:
            moveTop(r, c)
            moveBot(r,c)
            moveLeft(r, c)
            moveRight(r, c)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == False:
                    count+=1
        return count
            
                
        