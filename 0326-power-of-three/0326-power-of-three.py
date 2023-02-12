class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def pow_three(exponent):
            if pow(3, exponent) == n:
                return True
            if exponent > 31:
                return False
            return pow_three(exponent+1)
        return pow_three(-32)
            
            
        
        
        
        