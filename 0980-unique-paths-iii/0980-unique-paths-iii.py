class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        start_row,start_col,end_row,end_col = 0,0,0,0
        empty_cells = 0

        for i in range(0,rows):
            for j in range(0,cols):
                if (grid[i][j] == 1):
                    start_row,start_col = i,j
                elif (grid[i][j] == 2):
                    end_row,end_col = i,j
                elif (grid[i][j] == 0):
                    empty_cells += 1
        
        self.output = 0
        visited = set()

        def dfs(r,c,visited,walk):
            if (r == end_row and c == end_col):
                if (walk == empty_cells+1):
                    self.output += 1  # Path found
                return

            if (0<= r < rows and 0<= c < cols and grid[r][c] != -1 and (r,c) not in visited):
                visited.add((r,c))
                for i,j in [(0,-1),(0,1),(1,0),(-1,0)]:
                    dfs(r+i,c+j,visited,walk+1)
                visited.remove((r,c))
            
        dfs(start_row,start_col,visited,0)

        return self.output