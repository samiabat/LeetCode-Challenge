class Solution:
    def curstomPow(self, x, n):
        if n == 0: return 1
        half = self.curstomPow(x, n//2)
        return half * half * x ** (n%2)
    
    def myPow(self, x: float, n: int) -> float:
        if n >= 0: return self.curstomPow(x,n)
        return 1 / self.curstomPow(x,-n)
        
    
        
        