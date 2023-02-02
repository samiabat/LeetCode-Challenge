class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans =right=left=left2=cur=cur2 = 0
        while right < len(nums):
            cur += nums[right]
            cur2 += nums[right]
            while left<=right and cur >= goal:
                ans += (len(nums) - right)
                cur -= nums[left]
                left += 1
            while left2<=right and cur2 > goal:
                ans -= (len(nums) - right)
                cur2 -= nums[left2]
                left2 += 1
            right += 1
        return ans