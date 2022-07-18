class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 1
        n = len(nums)
        while p2<len(nums):
            if nums[p1]==nums[p2]:
                p2+=1
            else:
                nums[p1+1] = nums[p2]
                p1+=1
                p2+=1
        flag = False
        i = 0
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                flag=True
                break
        t = n-i
        if flag:
            for i in range(t):
                nums.pop()