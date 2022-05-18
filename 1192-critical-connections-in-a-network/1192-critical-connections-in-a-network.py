class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        m = [set() for _ in range(n)]
        for i, j in connections:
            m[i].add(j)
            m[j].add(i)
        s = set(tuple(el) for el in connections)
        seen = {}
        settled = set()
        def dfs(i = 0, last = None):
            if i in seen:
                return seen[i]
            elif i in settled:
                return float('inf')
            else:
                seen[i] = len(seen)
                ret = float('inf')
                for j in m[i]:
                    if j != last:
                        res = dfs(j, i)
                        if res < len(seen):
                            ret = min(ret, res)
                            for t in ((i, j), (j, i)):
                                if t in s:
                                    s.remove(t)
                                    
                del seen[i]
                
                settled.add(i)
                return ret
                
        dfs()
        return list(list(el) for el in s)
            
        
        