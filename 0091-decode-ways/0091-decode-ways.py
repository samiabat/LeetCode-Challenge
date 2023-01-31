class Solution:
    def numDecodings(self, s: str) -> int:
        if s == '0': return 0
        if len(s) == 1: return 1
        dp = [0] *  len(s)
        if s[-1] != '0': dp[-1] = 1
        if s[-2] != '0': dp[-2] = 1
        if s[-2] >'2' and s[-1] == '0': return 0
        if '0' not in s[-2:] and s[-2:]<= '26': dp[-2] = 2 
        for i in range(len(s)-3, -1, -1):
            if s[i] != '0':
                if s[i] < '2':
                    dp[i] = dp[i+1] + dp[i+2]
                elif s[i] == '2' and s[i+1] <='6':
                    dp[i] = dp[i+1] + dp[i+2]
                else:
                    dp[i] = dp[i+1]
            if s[i+1] > '2' and s[i+2] == '0':
                return 0
            if s[i] > '2' and s[i+1] == '0':
                return 0
        return dp[0]
            
            
            
                
        