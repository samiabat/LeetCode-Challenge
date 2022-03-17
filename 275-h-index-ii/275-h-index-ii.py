class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        r = len(citations)-1
        size = len(citations)
        while l<=r:
            m = (l+r)//2
            n = size-m
            print("m",m,"n",n)
            if citations[m]>=n and (m-1<0 or citations[m-1]<n+1):
                return n
            elif citations[m]>=n:
                r = m-1
            elif citations[m]<n:
                l = m+1
            else:
                r = m-1
        if len(citations)==1:
            if citations[0]>=1:
                return 1
            return 0
        if len(citations)==2:
            if citations[1]==0:
                return 0
        if citations==[0, 0, 0]:
            return 0
        return n
                