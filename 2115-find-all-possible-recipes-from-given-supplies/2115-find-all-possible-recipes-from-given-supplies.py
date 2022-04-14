class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = defaultdict()
        
        for i in range(len(ingredients)):
            for ing in ingredients[i]:
                graph[ing].append(recipes[i])
                if recipes[i] in indegree: 
                    indegree[recipes[i]]+=1
                else:
                    indegree[recipes[i]]=1
        q = deque(supplies)
        ans = []
        while q:
            top = q.popleft()
            for rec in graph[top]:
                indegree[rec]-=1
                if indegree[rec]==0:
                    q.append(rec)
                    ans.append(rec)
        return ans