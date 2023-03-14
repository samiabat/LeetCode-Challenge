class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def helper(l, r, turn):
            if l == r:
                return turn * nums[l]
            a = turn * nums[l] + helper(l + 1, r, -turn)
            b = turn * nums[r] + helper(l, r-1,  -turn)
            return turn * max(turn * a, turn * b)
        return helper(0, len(nums)-1, 1)>=0
		