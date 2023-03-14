class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def winner(l, r):
            if l == r: return nums[l]
            a = nums[l] - winner(l + 1, r)
            b = nums[r] - winner(l, r-1)
            return max(a, b)
        return winner(0, len(nums)-1)>=0
		