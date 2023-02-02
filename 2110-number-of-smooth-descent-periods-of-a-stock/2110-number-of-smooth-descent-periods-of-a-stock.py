class Solution:
    def getDescentPeriods(self, nums: List[int]) -> int:
        
        ans = 0
        cnt = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1] + 1:
                cnt += 1
            else:
                cnt += 1
                ans += cnt*(cnt + 1) // 2
                cnt = 0
        cnt += 1
        return ans + cnt*(cnt + 1) // 2
                
            
        