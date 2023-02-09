class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        cnt = Counter()
        ans = 0
        
        while right < len(nums):
            cnt[nums[right]] += 1
            
            while left<=right and len(cnt)>=k:
                ans += (len(nums) - right)
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
            right += 1
        cnt = Counter()
        left = 0
        right = 0
        while right < len(nums):
            cnt[nums[right]] += 1
            
            while left<=right and len(cnt)>k:
                ans -= (len(nums) - right)
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
            right += 1
        return ans
                
                