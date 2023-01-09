class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph,answer = defaultdict(list), -inf
        tot = defaultdict(int)
        for i in range(len(vals)):
            tot[i] = vals[i]
        if k == 0:
            return max(vals)
            
        for a, b in edges:
            if len(graph[a]) >= k:
                if graph[a][0] < vals[b]:
                    top = heappop(graph[a])
                    tot[a] -= max(top, 0)
                    heappush(graph[a], vals[b])
                    tot[a] += max(vals[b], 0)
            else:
                tot[a] += max(vals[b], 0)
                heappush(graph[a], vals[b])
                
            if len(graph[b]) >= k:
                if graph[b][0] < vals[a]:
                    top = heappop(graph[b])
                    tot[b] -= max(top, 0)
                    heappush(graph[b], vals[a])
                    tot[b] += max(vals[a], 0)
            else:
                tot[b] += max(vals[a], 0)
                heappush(graph[b], vals[a])
        for key in tot:
            answer = max(answer, tot[key])
        return answer
            
            
                
                
            
            
            