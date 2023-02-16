class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        s = list(s)
        n = len(s)
        dp = [[n+1 for _ in range(k+2)] for _ in range(n+1)]
        dp[0][0]=0
        for i in range(1, n+1):
            for j in range(0, k+1):
                count, delet, dp[i][j+1] = 0, 0, min(dp[i][j+1],dp[i-1][j])
                for l in range(i, n+1) :
                    if s[i-1] == s[l-1]: count += 1
                    else: delet += 1
                    if j + delet <= k:
                        length = dp[i-1][j] + 1
                        if count >= 100: length += 3
                        elif count >= 10: length += 2
                        elif count >= 2: length += 1
                        dp[l][j+delet] = min(dp[l][j+delet], length)
                    else: break
        return dp[n][k]