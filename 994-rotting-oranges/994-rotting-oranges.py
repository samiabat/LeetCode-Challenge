from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = deque()
        
        
        def can(grid, arr):
            r, c = arr[0], arr[1]
            return r>=0 and c>=0 and r<len(grid) and c<len(grid[0])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    que.append([i, j])
        print(que)
        count = 0
        while que:
            size = len(que)
            
            for _ in range(size):
                top = que.popleft()
                front = [top[0]-1,top[1]]                   
                bot = [top[0]+1,top[1]]
                right = [top[0],top[1]-1]
                left = [top[0],top[1]+1]                    
                newArr = [front, bot, right,left]
                for i in newArr:
                    if can(grid, i) and grid[i[0]][i[1]]==1:
                        grid[i[0]][i[1]] = 2
                        que.append(i)
            count+=1
        ans = set()
        for i in grid:
            for j in i:
                ans.add(j)
        if 1 in ans:
                return -1
        if 2 not in ans:
            return 0
        return count-1
            
    
        