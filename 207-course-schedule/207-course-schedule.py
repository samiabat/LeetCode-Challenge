class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        for src, dst in prerequisites:
            graph[dst].append(src)
            indegree[src]+=1
        q = deque([i for i in range(numCourses) if indegree[i]==0])
        if not q:
            return False
        while q:
            dst = q.popleft()
            for src in graph[dst]:
                indegree[src]-=1
                if indegree[src]==0:
                    q.append(src)
        for i in indegree:
            if i:
                return False
        return True