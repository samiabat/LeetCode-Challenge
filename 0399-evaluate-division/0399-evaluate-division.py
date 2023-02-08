class Solution:
    def calcEquation(self, eq, v, q):
        graph = defaultdict(dict)
        for i in range(len(eq)):
            graph[eq[i][0]][eq[i][1]] = v[i]
            graph[eq[i][1]][eq[i][0]] = 1 / v[i]
        def dfs(x, y, visited):
            if x not in graph or y not in graph:
                return -1.0
            if y in graph[x]:
                return graph[x][y]
            visited.add(x)
            for neighbor in graph[x]:
                if neighbor not in visited: 
                    temp = dfs(neighbor, y, visited)
                    if temp == -1.0:
                        continue 
                    return temp * graph[x][neighbor] 
            visited.remove(x)
            return -1.0 
        res = []
        for i, j in q:
            res.append(dfs(i, j, set()))
        return res 