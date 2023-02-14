class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        for i in range(n//2):
            arr.extend([-(i+1), i+1])
        if n%2: arr.append(0)
        return arr