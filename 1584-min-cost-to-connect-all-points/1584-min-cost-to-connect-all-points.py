class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        arr = []
        ans = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                md = abs(points[i][0]-points[j][0]) + abs(points[j][1]-points[i][1])
                arr.append((md, i, j))
        arr.sort()
        parents = [i for i in range(len(points))]
        def find(x):
            if parents[x]==x:
                return x
            return find(parents[x])
        for d in arr:
            dis, i1, i2 = d
            i1f = find(i1)
            i2f = find(i2)
            if i1f!=i2f:
                parents[i2f]=i1f
                ans+=dis
        return ans
            
            