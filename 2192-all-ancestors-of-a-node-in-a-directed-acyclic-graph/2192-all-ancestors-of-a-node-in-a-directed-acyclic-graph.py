class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0]*n
        
        for fr, to in edges:
            graph[fr].append(to)
            indegree[to]+=1
        q = deque([i for i in range(n) if indegree[i]==0])
        ans = [set() for _ in range(n  )]
        while q:
            top=q.popleft()
            for to in graph[top]:
                ans[to].add(top)
                ans[to] =  ans[to].union(ans[top])
                indegree[to]-=1
                if indegree[to]==0:
                    q.append(to)
        
        return [sorted(lst) for lst in ans ]