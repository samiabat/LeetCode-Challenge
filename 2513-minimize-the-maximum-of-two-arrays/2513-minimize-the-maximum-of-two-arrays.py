class Solution:
    def minimizeSet(self, d1: int, d2: int, u1: int, u2: int) -> int:
        def gain(num):return num - num // lcm(d1,d2) >= u1 + u2 and num - num // d1 >= u1 and num - num // d2 >= u2
        left, right = 1, pow(10, 10)
        while left <= right:
            mid = (left  + right) // 2
            if gain(mid): right = mid - 1
            else: left = mid + 1
        return left