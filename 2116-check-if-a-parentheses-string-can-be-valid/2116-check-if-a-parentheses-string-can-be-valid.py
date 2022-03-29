class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        low = high = 0
        for i in range(len(s)):
            if locked[i] == '1':
                if s[i] == '(':
                    low += 1
                    high += 1
                else:
                    low -= 1
                    high -= 1
            else:
                low -= 1
                high += 1
            low = max(low, 0)
            if low > high:
                return False
        return low == 0
                            