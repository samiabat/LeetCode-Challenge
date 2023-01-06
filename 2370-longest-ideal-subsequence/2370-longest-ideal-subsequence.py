class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = defaultdict(int)
        
        for i in range(len(s)):
            for j in range(max(ord('a'), ord(s[i]) - k), min(ord(s[i]) + k + 1, ord('z') + 1), 1):
                dp[s[i]] = max(dp[s[i]], dp[chr(j)])
            dp[s[i]] += 1
        return max(dp.values())
