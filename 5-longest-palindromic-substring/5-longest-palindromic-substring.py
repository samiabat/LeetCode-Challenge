class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        
        
        def dp(s, t, l, r):
            while l>0 and r<len(s)-1 and t[::-1] == t:
                l -= 1
                r += 1
                if s[r]==s[l]:
                    t =  s[l]+ t + s[r] 
                else:
                    break
            return t
        for i in range(len(s)):
            odd = dp(s, s[i], i, i)
            even = odd
            if i+1<len(s) and s[i]==s[i+1]:
                even= dp(s, s[i:i+2], i, i+1)
            res = max([odd, even, res], key = len)
        return res
        
        
        