class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = []
        ans = 0
        for num in nums:
            heappush(max_heap, -num)
        for _ in range(k):
            num = -heappop(max_heap)
            ans += num
            heappush(max_heap, 0 - math.ceil(num / 3))
        return ans