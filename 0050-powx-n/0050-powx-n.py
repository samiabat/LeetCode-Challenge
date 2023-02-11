class Solution:
    def pow(self, number, exponent):
        if exponent == 0: return 1
        if exponent == 1: return number
        half = self.pow(number, exponent // 2)
        if exponent % 2: return number * half * half
        return half * half
    
    
    def myPow(self, number, exponent):
        if exponent <= 0:
            return 1/(self.pow(number, -exponent))
        return self.pow(number, exponent)