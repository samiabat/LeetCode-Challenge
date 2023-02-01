class Solution:
    def numberOfWays(self, s: str) -> int:
        ans = 0
        one, zero, r_one, r_zero = int(s[0]), 1 - int(s[0]), s.count('1') - int(s[0]), s.count('0') - (1 - int(s[0]))
        
        for i in range(1, len(s) - 1):
            one += int(s[i])
            zero += (1 - int(s[i]))
            r_zero -= (1 - int(s[i]))
            r_one -= int(s[i])
            if s[i] == '0':
                ans += (one * r_one)
            elif s[i] == '1':
                ans += (zero * r_zero)
        return ans