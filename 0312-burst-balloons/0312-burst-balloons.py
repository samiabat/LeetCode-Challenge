class Solution:
    def maxCoins(self, ballons):
        length = len(ballons)
        dp = [[0 for j in range(length)] for i in range(length)]
        l = 0
        while l < length:
            i = 0
            while i + l < length:
                j = i + l
                leftBallon = ballons[i - 1] if i - 1 >= 0 else 1
                rightBallon = ballons[j + 1] if j + 1 < length else 1
                maxVal = -float('inf')
                for k in range(i, j + 1):
                    ksBurstCost = leftBallon * ballons[k] * rightBallon
                    if k == i:
                        # First in i <= k <= j
                        maxVal = max(maxVal, 0 + ksBurstCost + (dp[k + 1][j] if k + 1 < length else 0))
                    elif k == j:
                        # Last in i <= k <= j
                        maxVal = max(maxVal, dp[i][k - 1] + ksBurstCost + 0)
                    else:
                        # Mid in i <= k <= j
                        maxVal = max(maxVal, dp[i][k - 1] + ksBurstCost + dp[k + 1][j])
                dp[i][j] = maxVal
                i += 1
            l += 1
        return dp[0][length - 1]