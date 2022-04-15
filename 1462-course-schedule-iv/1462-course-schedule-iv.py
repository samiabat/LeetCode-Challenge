class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        
        
        for pre, cor in prerequisites:
            graph[pre].append(cor)
            indegree[cor]+=1
        q = deque([i for i in range(numCourses) if indegree[i]==0])
        ans = defaultdict(set)
        while q:
            pre = q.popleft()
            for cor in graph[pre]:
                indegree[cor]-=1
                ans[cor].add(pre)
                ans[cor].update(ans[pre])
                if indegree[cor]==0:
                    q.append(cor)
        fans = []
        for pre, cor in queries:
            fans.append(pre in ans[cor])
        return fans