class Solution:
    def restoreArray(self, ap: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visited = set()
        ans = []
        
        for a, b in ap:
            graph[a].append(b)
            graph[b].append(a)
            
        def dfs(node):
            visited.add(node)
            ans.append(node)
            for nbr in graph[node]:
                if nbr not in visited:
                    dfs(nbr)
        first = [key for key in graph if len(graph[key]) == 1]
        dfs(first[0])
        return ans