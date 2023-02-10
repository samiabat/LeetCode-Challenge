class Solution:
    def fib(self, n: int) -> int:
        if not n: return 0
        left = 1
        right = 1
        
        for i in range(2, n):
            left, right = right, left + right
        return right