class Solution:
    def fib(self, n: int) -> int:
        def helper(n):
            if n<=1:
                return (n, 0)
            (a,b) = helper(n-1)
            return (a+b, a)
        return helper(n)[0]