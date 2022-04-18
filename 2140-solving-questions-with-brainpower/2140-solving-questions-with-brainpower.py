class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        def dp(index):
            if index>len(questions)-1:
                return 0
            else:
                if index in memo:
                    return memo[index]
                points = questions[index][0]
                jump = questions[index][1]+1
                chose = points + dp(index+jump)
                notChose = dp(index+1)
                memo[index] = max(chose, notChose)
                return memo[index]
        return dp(0)