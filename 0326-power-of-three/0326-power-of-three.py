class Solution:
    def solve(self,i,n):
        if i == 0:return 1
        else: return 3 * self.solve(i-1,n)
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        val = ceil(log(n)/log(3))
        return n == self.solve(val,n)
            
        
        
        
        