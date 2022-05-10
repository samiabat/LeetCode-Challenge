class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
        if n > 45:
            return []
        
        elif k>n:
            return []
        def dp(index, arr = [], ans = []):
            if len(arr)==k and sum(arr)==n:
                ans.append(arr)
                return arr
            if len(arr)==k:
                return []
            if index>9:
                return []
            chose = dp(index+1, arr + [index], ans)
            notchose = dp(index+1, arr, ans)
            return ans
        return dp(1)
            
        