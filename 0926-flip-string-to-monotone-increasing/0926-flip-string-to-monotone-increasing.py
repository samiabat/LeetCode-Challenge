class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans, one, zero = min(s.count('1'), s.count('0')), 0, s.count('0')
        for i in range(len(s)):
            cur = (int(s[i]) == 1)       
            ans = min(ans, one + zero)
            one, zero = one + cur, zero - int(not cur) 
        return ans
            
            