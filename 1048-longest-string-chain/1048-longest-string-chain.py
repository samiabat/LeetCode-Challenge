class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def valid(b, a):
            cnt = 0
            i = j = 0
            while i<len(a) and j<len(b):
                if a[i]!=b[j]: 
                    cnt += 1
                    j += 1
                else:
                    i += 1
                    j += 1
            return ((cnt == 1 and i == len(a) and j == len(b)) or 
                    (not cnt and i == len(a) and j == len(b) - 1))
        
        words.sort(key = lambda x:len(x))
        words.reverse()
        
        dp = [1] * (len(words) + 1)
        
        ans = 0
        
        for i in range(len(words)-1, -1, -1):
            for j in range(i+1, len(words)):
                if len(words[i]) != len(words[j]) + 1: continue 
                if valid(words[i], words[j]):
                    dp[i] = max(dp[i], 1 + dp[j])
            ans = max(ans, dp[i])
        return ans
        