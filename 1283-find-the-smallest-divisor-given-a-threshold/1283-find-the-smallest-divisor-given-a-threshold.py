class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)+1
        dic = {}
        lis = []
        while l<=r:
            d = (l+r)//2
            t = nums.copy()
            for i in range(len(t)):
                t[i] = math.ceil(t[i]/d)
            tot = sum(t)
            t = (d, tot)
            lis.append(t)
            if tot>threshold:
                l = d+1
            elif tot<threshold:
                r = d-1
            else:
                r = d-1
                
        lis = sorted(lis)[::-1]
        d = lis[0][0]
        print(lis)
        for i in range(1, len(lis)):
            if lis[i][1]<=threshold:
                d = lis[i][0]
        return d