class Solution:
    def fourSum(self, nums, target):
        
        temp = len(nums)
        a = []
        for i in range(temp):
            for j in range(i, temp):
                for k in range(j, temp):
                    for w in range(k, temp):
                        if nums[i]+nums[j]+nums[k]+nums[w]==target:
                            a.append([nums[i],nums[j],nums[k],nums[w]])
        
        d = []
        
        for b in a:
            temp = len(b)
            status = "good"
            for c in range(temp):
                if b.count(b[c])>nums.count(b[c]):
                    status = "bad"
                    break
            if status == "good":
                d.append(b)
        w = []
        for i in d:
            i = sorted(i)
            if i not in w:
                w.append(i)
        return w
s = Solution()
s.fourSum([21, 12, 1, 2], 5)