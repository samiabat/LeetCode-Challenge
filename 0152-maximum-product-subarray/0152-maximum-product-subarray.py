class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0];cur = 1
        for num in nums:
            cur *= num
            ans = max(ans, cur)
            if cur == 0:cur = 1
                
        cur = 1
        other = nums[-1]
        for num in nums[::-1]:
            cur *= num
            other = max(other, cur)
            if cur == 0:cur = 1
        return max(ans, other)