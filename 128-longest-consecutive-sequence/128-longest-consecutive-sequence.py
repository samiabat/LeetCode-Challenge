class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp = set(nums)
        best = 0
        for i in nums:
            if i-1 in temp:
                continue
            else:
                count = 0
                j = i
                while j in temp:
                    count+=1
                    j+=1
                if count>best:
                    best = count
        return best
                