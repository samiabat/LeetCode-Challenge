class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = []
        arr = [str(i) for i in range(1, n+1)]
        def helper(n, k, prev, idx):
            if n == 1: 
                ans.append(arr[0])
                return
            if k <= factorial(n-1):
                ans.append(arr.pop(0))
                helper(n-1, k, 0, 1)
            else:
                arr[idx], arr[prev] = arr[prev], arr[idx]
                helper(n, k-factorial(n-1), prev, idx+1)
        helper(n, k, 0, 1)
        return ''.join(ans)
                
        