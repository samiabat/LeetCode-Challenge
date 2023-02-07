class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cur = 0
        for ele in logs:
            if ele== './': continue
            elif ele == '../' and cur: cur -= 1
            elif ele != '../': cur += 1
        return cur
            