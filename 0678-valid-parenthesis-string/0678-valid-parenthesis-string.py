class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[False]*n for i in range(n)]
        for i in range(n):
            if s[i]=="*":
                dp[i][i] = True
            
        for i in range(n-1):
            if s[i] in ["(","*"] and s[i+1] in [")","*"]:
                dp[i][i+1]=True
        
        for size in range(3,n+1):
            for i in range(n-size+1):
                j = i+size-1
                if dp[i+1][j-1] and (s[i] == "(" or s[i] == "*") and (s[j] == ")" or s[j] == "*"):
                    dp[i][j] = True
                
                for k in range(i,j):
                    if dp[i][k] and dp[k+1][j]:
                        dp[i][j]= True
                        
        return dp[0][n-1]
