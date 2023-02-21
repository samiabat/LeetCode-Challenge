class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n =len(grid), len(grid[0])
        ans=state=no_keys=0
        visited=set()
        locks={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5}
        keys={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5}
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='@':
                    q=deque([(i,j,0)])
                    visited.add((i,j,0))
                elif grid[i][j] in ascii_lowercase:
                    no_keys+=1
        while q:
            for _ in range(len(q)):
                x,y,state=q.popleft()
                val=grid[x][y]
                if (val in locks and (state & (1<<locks[val]))==0) or val=='#':
                    continue
                if val in keys:
                    state=state | (1<<keys[val])
                    if state==(1<<(no_keys))-1:
                        return ans
                for d in (0,1),(1,0),(0,-1),(-1,0):
                    nx,ny=x+d[0],y+d[1]
                    if 0<=nx<m and 0<=ny<n and (nx,ny,state) not in visited:
                        visited.add((nx,ny,state))
                        q.append((nx,ny,state))
            ans+=1
        return -1
