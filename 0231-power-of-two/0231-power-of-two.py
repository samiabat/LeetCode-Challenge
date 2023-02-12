class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0: return False
        def check_pow(exponet):
            if exponet > 32: return False
            if pow(2, exponet) == n:
                return True
            return check_pow(exponet + 1)
        return check_pow(0)
        
        
                