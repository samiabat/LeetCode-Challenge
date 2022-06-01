class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if not i:
                continue
            else:
                nums[i] +=nums[i-1]
        return nums