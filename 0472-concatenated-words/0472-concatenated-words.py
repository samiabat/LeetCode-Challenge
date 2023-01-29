class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        st = set(words)
        ans = []
        for word in words:
            dp = [0] * (len(word)  + 1)
            dp[-1] = 1
            for i in range(len(word)-1, -1, -1):
                for j in range(i, len(word)):
                    if word[i:j+1] in st and dp[j+1]:
                        dp[i] = max(dp[i], 1 + dp[j+1])
            if dp[0] > 2: ans.append(word)
        return ans
            
        
        