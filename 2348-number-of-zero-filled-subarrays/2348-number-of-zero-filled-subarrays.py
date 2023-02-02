class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt += 1
            else:
                ans += cnt * (cnt + 1) // 2
                cnt = 0
        return ans + cnt * (cnt + 1) // 2