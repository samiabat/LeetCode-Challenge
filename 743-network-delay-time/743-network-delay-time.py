class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        
        for x,y,w in times:
            graph[x].append((w, y))
        
        visited=[False]*(n+1)
        heap = [(0, k)]
        
        i = 0
        
        while heap:
            tt, node = heapq.heappop(heap)
            
            if visited[node] == True:
                continue
            
            visited[node] = True
            i += 1
            
            if i == n:
                return tt
            
            for t, nbr in graph[node]:
                if visited[nbr] == False:
                    heapq.heappush(heap, (tt+t, nbr))
                
        return -1