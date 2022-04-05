
class Solution:
    def fact(self,n):
        if n==1 or n==0:
            return n
        else:
            return n*self.fact(n-1)
    def countOrders(self, n: int) -> int:
        return (self.fact(2*n)//2**n)%(10**9+7)