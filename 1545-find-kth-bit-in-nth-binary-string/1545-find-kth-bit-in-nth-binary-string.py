class Solution:
    def reverse(self, s):
        return s[::-1]
    def invert(self, s):
        s = list(s)
        for i in range(len(s)):
            if s[i] == '1': s[i] = '0'
            else: s[i] = '1'
        return ''.join(s)
    def kthbit(self,n):
        if n == 1: return '0'
        prev = self.kthbit(n-1)
        return prev + "1" + self.reverse(self.invert(prev))
    def findKthBit(self, n: int, k: int) -> str:
        return self.kthbit(n)[k-1]
        
    