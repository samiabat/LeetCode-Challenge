class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = []
        arr = [str(i) for i in range(1, n+1)]
        m = n
        def helper(n, k, prev, idx):
            if k == 0: 
                ans.extend(sorted(arr))
                return
            if n>= 1 and k <= factorial(n-1):
                ans.append(arr[prev])
                arr.pop(0)
                arr.sort()
                helper(n-1, k, 0, 1)
            else:
                if idx >= len(arr): return 
                arr[idx], arr[prev] = arr[prev], arr[idx]
                helper(n, k-factorial(n-1), prev, idx+1)
        helper(n, k, 0, 1)
        return ''.join(ans)
                
        