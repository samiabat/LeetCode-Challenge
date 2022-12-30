class Solution:
    def maxPoints (self, grid: List[List[int]], queries: List[int]) -> List[int]:
        graph = defaultdict(list)
        valid = lambda x, y: 0<=x<len(grid) and 0<=y<len(grid[0])
        arr = []
        heap = [(grid[0][0], (0, 0))]
        visited = set()

        while heap:
            val, top = heappop(heap)
            visited.add(top)
            arr.append(val)
            for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = top[0] + i, top[1] + j
                if not valid(nx, ny) or (nx, ny) in visited: continue
                visited.add((nx, ny))
                heappush(heap, (grid[nx][ny], (nx, ny)))
        for i in range(1, len(arr)):
            arr[i] = max(arr[i], arr[i-1])
        ans = []

        for i in range(len(queries)):
            idx = bisect_right(arr, queries[i]-1)
            ans.append(idx)
        return ans

