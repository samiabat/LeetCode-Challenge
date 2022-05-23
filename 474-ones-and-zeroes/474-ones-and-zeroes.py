class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counter = Counter([(s.count('0'), s.count('1')) for s in strs])
        d = defaultdict(lambda: -1)
        
        def dfs(m, n, count):
            if d[(m, n)] >= count: return d[(m, n)]
            max_count = count
            d[(m, n)] = count
            
            for k, v in counter.items():
                if v <= 0: continue
                zeros, ones = k[0], k[1]
                if zeros <= m and ones <= n:
                    counter[k] -= 1
                    max_count = max(max_count, dfs(m - zeros, n - ones, count + 1))
                    counter[k] += 1
            return max_count        
        result = dfs(m, n, 0)
        return result