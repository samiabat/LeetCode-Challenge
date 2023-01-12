class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        
        for a, b, c in roads:
            graph[a].add((b, c))
            graph[b].add((a, c))
        
        answer = [inf]
        visited = set()
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for nbr, c in graph[node]:
                answer[0] = min(answer[0], c)
                dfs(nbr)
        dfs(1)
        return answer[0]
            