class Solution:
	def PredictTheWinner(self, nums: List[int]) -> bool:
		@lru_cache(None)
		def dp(i, j, turn):
			if i > j:
				return 0
			if turn == 0:
				return max(nums[i] + dp(i+1,j,1), nums[j] + dp(i,j-1,1))
			else:
				return min(dp(i+1,j,0), dp(i, j-1, 0))

		tot = sum(nums)
		p1 = dp(0, len(nums)-1, 0)
		p2 = tot-p1
		return p1>=p2