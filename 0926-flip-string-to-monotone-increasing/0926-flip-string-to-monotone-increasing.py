class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans, one, zero = min(s.count('1'), s.count('0')), 0, s.count('0')
        for i in range(len(s)):
            one, zero, ans = one + int(s[i]), zero - (int(s[i]) ^ 1), min(ans, one + zero)
        return ans
            
            