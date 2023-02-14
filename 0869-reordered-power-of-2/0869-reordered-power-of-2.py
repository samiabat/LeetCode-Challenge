from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        length = len(str(n))
        c = Counter(str(n))
        for i in range((length-1) * 3 + length // 3, length * 3 + length // 3 + 1):
            candidate = str(1 << i)
            if c == Counter(candidate):
                return True
        return False