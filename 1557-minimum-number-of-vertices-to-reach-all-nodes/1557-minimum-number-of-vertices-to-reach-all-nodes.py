class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict()
        for a,b in edges:
            graph[a].append(b)
            if b in indegree:
                indegree[b]+=1
                continue
            indegree[b] = 1
        ans = []
        for i in range(n):
            if i not in indegree:
                ans.append(i)
        return ans
            
            