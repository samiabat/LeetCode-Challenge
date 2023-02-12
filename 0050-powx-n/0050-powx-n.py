class Solution:
    def pow(self, x, n):
        if n == 1: return x
        half = pow(x, n//2) 
        if n % 2 == 1:
            return x * half * half
        return half*half
    def myPow(self, x: float, n: int) -> float:
        if n>0: return self.pow(x, n)
        elif n<0: return self.pow(1/x, -n)
        else: return 1
        
        
        