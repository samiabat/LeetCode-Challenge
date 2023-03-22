class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = [str(i) for i in range(1, n+1)]
        return ''.join(sorted(permutations(arr))[k-1])
        