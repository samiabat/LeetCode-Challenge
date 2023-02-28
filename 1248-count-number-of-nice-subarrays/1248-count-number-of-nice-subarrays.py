class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        left = 0
        right = 0
        left1 = 0
        
        
        ods = 0 
        ods2 = 0
        
        ans = 0
        while right < len(nums):
            ods  += int(nums[right] % 2)
            ods2 += int(nums[right] % 2)
            
            while left <= right and ods >= k:
                ans += (len(nums) - right)
                ods -= int(nums[left] % 2)
                left += 1
                
            while left1 <= right and ods2 > k:
                ans -= (len(nums) - right)
                ods2 -= int(nums[left1] % 2)
                left1 += 1
                
            right += 1
            
        return ans
            
             