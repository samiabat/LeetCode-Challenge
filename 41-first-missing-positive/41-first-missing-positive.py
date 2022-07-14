class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ma = max(nums)
        if ma<=0:
            return 1
        s = set(nums)
        
        for i in range(1, ma):
            if i not in s:
                return i
        return ma+1
        