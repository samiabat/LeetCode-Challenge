class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def recursion(i):
            if i >= 31:return False
            if  pow(4, i) == n: return True
            return recursion(i+1)
        return recursion(0)
        
        
        