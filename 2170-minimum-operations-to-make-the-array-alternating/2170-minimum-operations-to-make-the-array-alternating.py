from collections import Counter
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        arr = []
        arr2 = []
        for i in range(len(nums)):
            if i%2:
                arr.append(nums[i])
            if not i%2:
                arr2.append(nums[i])
        dic1 = Counter(arr)
        dic2 = Counter(arr2)
        m1, m2, m3, m4 = inf, inf, inf, inf
        for i in dic1:
            if dic1[i]>dic1[m1]:
                m1, m3 = i, m1
                continue
            if dic1[i] > dic1[m3]:
                m3 = i
        for i in dic2:
            if dic2[i]>dic2[m2]:
                m2, m4 = i, m2
                continue
            if dic2[i]>dic2[m4]:
                m4 = i
        if m1==m2:
            if dic1[m1] + dic2[m4] > dic1[m3] + dic2[m2]:
                m1, m2 = m1, m4
            else:
                m1, m2 = m3, m2
        return len(nums)-dic1[m1]-dic2[m2]     