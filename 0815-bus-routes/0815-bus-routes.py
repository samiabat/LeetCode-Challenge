class Solution:
    def numBusesToDestination(self, rt, src, tar):
        if src == tar:
            return 0
        mp = defaultdict(set)
        for i in range(len(rt)):
            for s in rt[i]:
                mp[s].add(i) 
        arr = []
        for r in mp[src]:
            arr.append([r, 1])
        visited = set()
        visited.add(r)
        while arr:
            nxt = []
            for r, n in arr:
                for s2 in rt[r]:
                    if s2 == tar:
                        return n
                    for r2 in mp[s2] - visited:
                        nxt.append([r2, n+1])
                        visited.add(r2)
            arr = nxt[:]
        return -1