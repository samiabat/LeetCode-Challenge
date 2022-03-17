class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        Do not return anything, modify board in-place instead.
        """
        visit = []
        arr = []
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m):
            visit.append([False]*n)
        for i in range(m):
            visit.append([False]*n)
        count = 0
        def dfs(grid, visit, r, c):
            if r>=0 and c>=0 and r< len(grid) and c<len(grid[0]):
                if not visit[r][c] and grid[r][c]==1:
                    visit[r][c]=True
                    arr.extend([(r, c)])
                    dfs(grid, visit, r+1, c)
                    dfs(grid, visit, r-1, c)
                    dfs(grid, visit, r, c+1)
                    dfs(grid, visit, r, c-1)        
        for i in range(m):
            for j in range(n):
                if not visit[i][j]:
                    dfs(grid, visit, i, j)
                    if grid[i][j]==1:
                        count+=1
                        arr.append(0)
        def check(arr, r, c):
            for i in arr:
                if i[0]==0 or i[1]==0 or i[0]==r-1 or i[1]==c-1:
                    return 0
            return len(arr)
        st = []
        for i in arr:
            if i:
                st.append(i)
            else:
                ans+=check(st, m, n)
                st = []
        return ans
        