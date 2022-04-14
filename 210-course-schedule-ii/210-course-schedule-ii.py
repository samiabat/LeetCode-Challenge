class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        
        for dst, src in prerequisites:
            graph[src].append(dst)
            indegree[dst] +=1
        q  = deque([i for i in range(numCourses) if indegree[i]==0])
        if not q:
            return []
        ans = []
        while q:
            src = q.popleft()
            ans.append(src)
            for dst in graph[src]:
                indegree[dst]-=1
                if indegree[dst]==0:
                    q.append(dst)
        for i in indegree:
            if i:
                return []
        return ans