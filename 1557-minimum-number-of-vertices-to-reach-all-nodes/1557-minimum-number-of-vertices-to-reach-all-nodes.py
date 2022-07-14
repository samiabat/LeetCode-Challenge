class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        prt = {}
        for a,b in edges:
            if a not in prt:
                prt[a]=0
            prt[b]=1
            graph[a].append(b)
        return [i for i in prt if prt[i]==0]
            
            