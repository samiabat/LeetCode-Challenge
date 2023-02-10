class Solution:
    def numOfPairs(self, nums, t):
        cnt = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == t:
                        cnt += 1
        return cnt