class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums  = sorted(nums)
        output = [""] * len(nums)
        for i,each in enumerate (nums):
             output[i] = sortedNums.index(each)
        return output