class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dp(t, res=[]):
            if t==0:
                ans.append(res)
                return
            if t<0:
                return
            for i in candidates:
                dp(t - i, res + [i])
        dp(target)
        ans = [tuple(sorted(i)) for i in ans]
        return set(ans)