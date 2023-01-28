class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        cur =  0
        ans = 0
        while right < len(nums):
            cur += nums[right]
            while left<=right and cur >= target:
                if not ans: ans = right - left + 1
                else: ans = min(ans, right - left + 1)
                cur -= nums[left]
                left += 1
            right += 1
        return ans
            