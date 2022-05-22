class Solution:
    def countSubstrings(self, s: str) -> int:
        self.slen = len(s)
        self.count = 0
        def dfs(l, r):
            if l >= 0 and r < self.slen and s[l] == s[r]:
                self.count += 1
                dfs(l-1, r+1)
        for i in range(self.slen):
            dfs(i, i)
            dfs(i, i+1)
        return self.count