class Solution:
    def minimumDeletions(self, s: str) -> int:
        a = s.count('a')
        b = s.count('b')
        la = 0
        lb = 0
        ans = inf 
        for i in range(len(s)):
            ans = min(ans, a+lb)
            a -= int(s[i] == 'a')
            b -= int(s[i] == 'b')
            la += int(s[i] == 'a')
            lb += int(s[i] == 'b')
        return min(ans, a + lb)
            