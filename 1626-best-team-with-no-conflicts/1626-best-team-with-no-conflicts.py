class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        dp = [0] * (len(scores))        
        scores = list(zip(scores, ages))
        scores.sort()
        ans = 0
        for i in range(len(scores)-1, -1, -1):
            dp[i] = scores[i][0]
            for j in range(i+1, len(scores)):
                if scores[i][1] <= scores[j][1]:
                    dp[i] = max(dp[i], scores[i][0] + dp[j])
            ans=max(ans, dp[i])
        return ans