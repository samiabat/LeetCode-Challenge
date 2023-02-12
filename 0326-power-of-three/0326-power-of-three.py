class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(-31, 32, 1):
            if pow(3, i) == n:
                return True
        return False
        
        
        
        