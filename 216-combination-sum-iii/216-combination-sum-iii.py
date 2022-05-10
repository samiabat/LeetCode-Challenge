class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dp(index, arr = [], ans = []):
            if len(arr)==k and sum(arr)==n:
                ans.append(arr)
                return arr
            if len(arr)==k:
                return
            if index>9:
                return
            chose = dp(index+1, arr + [index], ans)
            notchose = dp(index+1, arr, ans)
            return ans
        return dp(1)
            
        