class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        newgraph = defaultdict(list)
        indegree=[0]*len(graph)
        for src in range(len(graph)):
            for dst in graph[src]:
                newgraph[dst].append(src)
                indegree[src]+=1
        ans = [i for i in range(len(graph)) if indegree[i]==0]
        q = deque(ans)
        while q:
            top = q.popleft()
            for src in newgraph[top]:
                indegree[src]-=1
                if indegree[src] == 0:
                    q.append(src)
                    ans.append(src)
        ans.sort()
        return ans
        
                
          