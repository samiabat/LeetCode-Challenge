class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int: 
        def dfs(isConnected, i, visit):
            visit[i] = True
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and not visit[j]:
                    dfs(isConnected, j, visit)
        n = len(isConnected)
        count = 0
        visit = [False] * n 
        for i in range(n):
            if not visit[i]:
                dfs(isConnected, i, visit)
                count += 1
        
        return count