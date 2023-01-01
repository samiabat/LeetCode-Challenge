class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        i, ans, n, cur = 0, 0, len(s), ''
        while i < n:
            if int(cur + s[i]) < k:
                cur += s[i]
                i += 1
            elif int(cur + s[i]) == k:
                ans += 1
                cur = ''
                i += 1
            elif cur and int(cur) <= k:
                ans += 1
                cur = ''
            else:
                return -1
        return ans + 1 if cur else ans