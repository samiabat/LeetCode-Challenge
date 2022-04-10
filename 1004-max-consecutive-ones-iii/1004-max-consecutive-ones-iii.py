class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        j = 0
        newAns = 0
        while j<len(nums)and (nums[j] or k>0): 
                newAns+=1
                if not nums[j]:
                    k-=1
                j+=1
        left = 0
        right = j
        ans = newAns
        i = 1
        while left < len(nums):
            if nums[left]==0:
                k+=1
            else:
                k = 0
            newAns-=1
            left += 1
            while right<len(nums) and (nums[right]==1 or k>0):
                newAns+=1
                if not nums[right]:
                    k-=1
                right+=1
            if newAns>ans:
                ans = newAns
        return ans
                