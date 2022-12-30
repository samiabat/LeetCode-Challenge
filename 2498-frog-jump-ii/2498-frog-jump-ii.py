class Solution:
    def maxJump(self, stones: List[int]) -> int:
        ans, n = stones[1] - stones[0], len(stones)
        for i in range(2, n):
            ans = max(ans, stones[i] - stones[i-2])
        return ans